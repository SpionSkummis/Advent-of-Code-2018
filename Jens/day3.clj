;; Read input to a seq of seqs on the form (id left-edge top-edge width height)
(def day3input (->> (re-seq #"\#(\d+)\s\@\s(\d+)\,(\d+)\:\s(\d+)x(\d+)" (slurp "./day3input.txt"))
	(map (partial drop 1))
	(map #(map read-string %))))

;; Day 3-1. Slow and ugly, but what the hell.
(defn get-rectangle-coords [left top width height]
	(let [max-hor (->> day3input (map #(+ (nth % 1) (nth % 3))) (apply max))]
	(for [y (range top (+ top height)) x (range left (+ left width))] (+ (* y max-hor) x))))

(->> day3input
	;; Drop the id
	(map (partial drop 1))
	;; Get all of the rectangle coordinates, count the ones occuring more than once
	(map (partial apply get-rectangle-coords))
	(reduce concat)
	frequencies
	(remove #(= 1 (second %)))
	count)

;; Day 3-2. Also slow and ugly.
(defn overlap? [[x1 y1 w1 h1] [x3 y3 w2 h2]]
	(let [x2 (+ x1 w1) y2 (+ y1 h1) x4 (+ x3 w2) y4 (+ y3 h2)] 
	(if (not= 0 (* (min 0 (- (max x1 x3) (min x2 x4))) (min 0 (- (max y1 y3) (min y2 y4))))) true false)))

(loop [current (first day3input)]
	(let [the-rest (concat (take (- (first current) 1) day3input) (drop (first current) day3input))
		overlap (->> (map #(vector %1 %2) (map #(overlap? (drop 1 current) (drop 1 %)) the-rest) the-rest)
			(reduce #(if (true? (first %1)) %1 %2)))]
		(if (true? (first overlap))
			(recur (nth day3input (first current)))
			(first current))))

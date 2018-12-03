;; Read input to a list of vectors on the form [full-string id left-edge top-edge width height]
(def day3input (re-seq #"\#(\d+)\s\@\s(\d+)\,(\d+)\:\s(\d+)x(\d+)" (slurp "./day3input.txt")))
;; Calculate max horizontal coord
(def max-hor (->> day3input
	(map #(vector (nth % 2) (nth % 4)))
	(map #(map read-string %))
	(map (partial apply +))
	(apply max)))

;; Day 3-1. Slow and ugly, but what the hell.
(defn get-rectangle-coords [left top width height]
	(for [y (range top (+ top height)) x (range left (+ left width))] (+ (* y max-hor) x)))

(->> day3input
	;; Get rid of unnecessary fields, parse remaining fields to ints
	(map (partial drop 2))
	(map #(map read-string %))
	;; Get all of the rectangle coordinates, count the ones occuring more than once
	(map (partial apply get-rectangle-coords))
	(reduce concat)
	frequencies
	(remove #(= 1 (second %)))
	count)

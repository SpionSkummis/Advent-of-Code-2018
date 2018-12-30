;; Read input into list of vectors :: ([x y] ...)
(def day6input (->> (re-seq #"(\d+),\s(\d+)" (slurp "./day6input.txt"))
	(map (partial drop 1))
	(map (partial map read-string))
	(map (partial apply vector))))

;; Store the lower left and upper right corners of the bounding box containing all points :: {:x-min :y-min :x-max :y-max}
(def bounds (let [coll day6input] {
	:x-min (apply min (map first coll))
	:y-min (apply min (map second coll))
	:x-max (apply max (map first coll))
	:y-max (apply max (map second coll))}))

;; Manhattan distance between two points :: [x y] -> [x y] -> int
(defn distance [[x1 y1][x2 y2]]
	(+ (Math/abs (- x1 x2)) (Math/abs (- y1 y2))))

;; Closest point to current from list points, if equal distance returns nil :: [x y] -> ([x y] ...) -> [x y]
(defn closest [current points]
	(->> (map #(vector (distance current %) %) points)
		(sort-by first)
		(#(if (= (first (first %)) (first (second %))) nil (second (first %))))))

;; Any point that is closest to a point on the bounding box will be infinite. List of all such points. :: ([x y] ...)
(def infinite
	(filter some? (distinct (concat
		(for [x (range (bounds :x-min) (inc (bounds :x-max)))]
			(closest [x (bounds :y-min)] day6input))
		(for [x (range (bounds :x-min) (inc (bounds :x-max)))]
			(closest [x (bounds :y-max)] day6input))
		(for [y (range (bounds :y-min) (inc (bounds :y-max)))]
			(closest [(bounds :x-min) y] day6input))
		(for [y (range (bounds :y-min) (inc (bounds :y-max)))]
			(closest [(bounds :x-max) y] day6input))))))

(->> (filter some? (for [x (range (inc (bounds :x-min)) (bounds :x-max))
	y (range (inc (bounds :y-min)) (bounds :y-max))]
	(closest [x y] day6input)))
	(remove #(some (partial = %) infinite))
	frequencies
	(sort-by second)
	last
	second
)

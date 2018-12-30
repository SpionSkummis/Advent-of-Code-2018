(def day10input
  (let [raw-input (vec (map read-string (re-seq #"\-*\d+" (slurp "./day10input.txt"))))]
    (loop [i 0 input []] (if (< i (count raw-input)) (recur (+ i 4) (conj input (subvec raw-input i (+ i 4)))) input))))

;; Apply the velocities of the stars to their current positions and get their new positions :: [[int int int int] ...] -> [[int int int int] ...]
(defn move-step [input] (mapv (fn [[x-pos y-pos x-vel y-vel]] [(+ x-pos x-vel) (+ y-pos y-vel) x-vel y-vel]) input))

;; Functions for getting min and max values from vector of positions
(defn max-x [input] (apply max (mapv first input)))
(defn min-x [input] (apply min (mapv first input)))
(defn max-y [input] (apply max (mapv second input)))
(defn min-y [input] (apply min (mapv second input)))

(defn area [input] (* (- (max-x input) (min-x input))
                      (- (max-y input) (min-y input))))

;; Position and time of the step which requires the smallest area to contain all stars :: [[[int int int int] ...] int]
(def final-positions-and-time
  (loop [positions (move-step day10input)
         prev-area (area day10input)
         prev-positions day10input
         time 0]
    (if (> (area positions) prev-area)
      [prev-positions time]
      (recur (move-step positions) (area positions) positions (inc time)))))

;; The final positions of the stars :: [[int int] ...]
(def final-positions (mapv #(vector (first %) (second %)) (first final-positions-and-time)))

;; Day 10-1

;; Output a vector of strings 
(def output (for [y (range (min-y final-positions) (inc (max-y final-positions)))
                  x (range (min-x final-positions) (inc (max-x final-positions)))]
              (if (some #(= [x y] %) final-positions)
                (str "#" (when (= x (max-x final-positions)) "\n"))
                (str "." (when (= x (max-x final-positions)) "\n"))))) 

;; Print the resulting image
(println (apply str output))

;; Day 10-2
(second final-positions-and-time)

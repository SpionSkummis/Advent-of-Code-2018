(def day14input 637061)

(def starting-recipes [3 7])

;; Given the two current recipes, returns a vector of the resulting recipe(s) :: int -> int -> [int ...]
(def make-recipes (memoize (fn [elf-1-current elf-2-current]
  (let [sum (+ elf-1-current elf-2-current)]
    (if (> sum 9)
      [1 (- sum 10)]
      [sum])))))

;; Day 14-1
;; Generates ten more recipes than end and returns those ten :: int -> [int ...]
(defn ten-after [end]
  (loop [recipes starting-recipes elf-1-pos 0 elf-2-pos 1 n (count recipes)]
    (if (<= (+ 10 end) n)
      (subvec recipes end (+ 10 end))
      (let [elf-1-recipe (nth recipes elf-1-pos)
            elf-2-recipe (nth recipes elf-2-pos)
            new-recipes (into recipes (make-recipes elf-1-recipe elf-2-recipe))]
        (recur new-recipes
               (mod (+ 1 elf-1-pos elf-1-recipe) (count new-recipes))
               (mod (+ 1 elf-2-pos elf-2-recipe) (count new-recipes))
               (count new-recipes))))))

(ten-after day14input)

;; Day 14-2
(def input-vector (vec (map read-string (clojure.string/split (str day14input) #""))))

;; Continues generating new recipes while sliding a window of the same length as target over the vector until it finds a match. Returns number of passed elements. :: [int ... ] -> int
(defn first-occurence [target]
  (loop [recipes starting-recipes elf-1-pos 0 elf-2-pos 1 not-before (- (count starting-recipes) (count target))]
    (if (= target (subvec recipes (max 0 not-before)
                          (min (+ (max 0 not-before) (count target)) (count recipes))))
      not-before
      (let [elf-1-recipe (nth recipes elf-1-pos)
            elf-2-recipe (nth recipes elf-2-pos)
            new-recipes (into recipes (make-recipes elf-1-recipe elf-2-recipe))]
        (recur new-recipes
               (mod (+ 1 elf-1-pos elf-1-recipe) (count new-recipes))
               (mod (+ 1 elf-2-pos elf-2-recipe) (count new-recipes))
               (inc not-before))))))

(first-occurence input-vector)

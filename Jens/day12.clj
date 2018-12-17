(def day12input (slurp "./day12input.txt"))

;; A hash-map of the initial state of the pots (pot number as key). 1 means plant, 0 means no plant. :: {int int, ...}
(def initial-state
  (reduce merge
          (map #(hash-map %1 %2)
               (range)
               (replace {\# 1 \. 0} (re-find #"[\#\.]{6,}" day12input)))))

;; Given an input (int int int int int), interprets it as a binary number and returns its value :: (int int int int int) -> int
(defn relative-sum [five-pots] (reduce + (map * five-pots [16 8 4 2 1])))

;; The sums of combinations of five pots that will result in a plant in the middle pot :: (int ...)
(def new-plant (map relative-sum
                    (map (partial replace {\# 1 \. 0})
                         (map second (re-seq #"([\.\#]{5}) \=\> \#" day12input)))))

;; Given the sum of five pots, returns true if the middle pot grows (nil otherwise) :: int -> bool?
(defn grow? [sum] (some (partial = sum) new-plant))

;; Given a pot number and the state, returns the contents of the five pots where the supplied pot is in the middle :: int -> {int int, ...} -> (int int int int int)
(defn get-five-pots [pot state]
  (map #(if (contains? state %) (state %) 0) (range (- pot 2) (+ pot 3))))

;; Applies the rules for plant growth on the pots defined by state and returns the new state :: {int int, ...} -> {int int, ...}
(defn advance-generation [state]
  (let [state-keys (sort (keys state))
        first-pot (first state-keys)
        second-pot (second state-keys)
        last-pot (first (reverse state-keys))
        second-to-last-pot (second (reverse state-keys))
        start (if (= 1 (state first-pot)) (- first-pot 2)
                           (if (= 1 (state second-pot)) (dec first-pot)
                               first-pot))
        stop (if (= 1 (state last-pot)) (+ last-pot 2)
                          (if (= 1 (state second-to-last-pot)) (inc last-pot)
                              last-pot))]
    (loop [i start new-state {}]
      (if (> i stop)
        new-state
        (recur (inc i)
               (assoc new-state i (if (grow? (relative-sum (get-five-pots i state))) 1 0)))))))

;; Sums the numbers of all the pots with plants in state :: {int int, ...} -> int
(defn gen-sum [state] (reduce + (map #(* (first %) (second %)) (vec state))))

;; Sums the first number-of-generations generations. Assumes the increasing sum will converge to a linear function for large numbers of generations. :: int -> {int int, ...} -> int
(defn sum-generations [number-of-generations]
   (loop [generation 0 state initial-state prev-sum 0 delta 0 similar-deltas 0]
     (let [new-delta (- (gen-sum state) prev-sum)]
       ;; If the last ten generations have the same delta, assume the rest will as well and don't simulate them.
       (if (= similar-deltas 10)
         (+ (* (- number-of-generations generation) delta) (gen-sum state))
         ;; Return gen-sum if we're at the final generation
         (if (= generation number-of-generations)
           (gen-sum state)
           ;; Recur, updating generation, sum and deltas
           (recur (inc generation)
                  (advance-generation state)
                  (gen-sum state)
                  new-delta
                  (if (= new-delta delta) (inc similar-deltas) 0)))))))

;; Day 12-1
(sum-generations 20)

;; Day 12-2
(sum-generations 50000000000)

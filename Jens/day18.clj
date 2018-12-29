(def day18input (apply list (remove #(= \newline %) (slurp "./day18input.txt"))))

(def starting-woods
  (loop [x -1 y -1 remaining day18input woods {}]
    (if (= 51 y)
      woods
      (let [no-char (or (= x -1) (= y -1) (= x 50) (= y 50))
            to-add  (if no-char \. (peek remaining))]
        (recur (if (= x 50) 0 (inc x))
               (if (= x 50) (inc y) y)
               (if no-char remaining (pop remaining))
               (assoc-in woods [x y] to-add))))))

(defn adjacent-acres [woods x-pos y-pos]
  "Takes a map representing the woods and x and y coordinates. Returns the contents of the eight adjacent acres."
  (map #((woods %1) %2)
       [(dec x-pos) x-pos (inc x-pos) (dec x-pos) (inc x-pos) (dec x-pos) x-pos (inc x-pos)]
       [(dec y-pos) (dec y-pos) (dec y-pos) y-pos y-pos (inc y-pos) (inc y-pos) (inc y-pos)]))

(defmulti grow-acre (fn [woods x-pos y-pos] ((woods x-pos) y-pos)))
(defmethod grow-acre \. [woods x-pos y-pos]
  (if (<= 3 (count (filter #(= \| %) (adjacent-acres woods x-pos y-pos)))) \| \.))
(defmethod grow-acre \| [woods x-pos y-pos]
  (if (<= 3 (count (filter #(= \# %) (adjacent-acres woods x-pos y-pos)))) \# \|))
(defmethod grow-acre \# [woods x-pos y-pos]
  (if (and
       (<= 1 (count (filter #(= \# %) (adjacent-acres woods x-pos y-pos))))
       (<= 1 (count (filter #(= \| %) (adjacent-acres woods x-pos y-pos)))))
    \# \.))

(defn minute [woods]
  "Simulates one minute of wood growth in woods."
  (loop [x 0 y 0 after-growth woods]
    (if (= y 50) ; When y overflows, we're done
      after-growth
      (recur (if (= x 49) 0 (inc x))
             (if (= x 49) (inc y) y)
             (assoc-in after-growth [x y] (grow-acre woods x y)))))) ; Add the newly grown acre to the new representation of the woods

(defn resource-value [woods]
  (* (count (filter #(= \| %) (mapcat vals (vals woods))))
     (count (filter #(= \# %) (mapcat vals (vals woods))))))

;; Day 18-1
(loop [i 0 woods starting-woods]
  (if (= i 10) ; Break after 10 minutes
    (resource-value woods)
    (recur (inc i) (minute woods))))

;; Day 18-2
(def number-of-minutes 1000000000)

(def repeating-pattern
  (let [[first-repeat seen] (loop [woods starting-woods seen []]
                              (if (some #(= woods %) seen)
                                [woods seen]
                                (recur (minute woods)
                                       (conj seen woods))))
        start (reduce #(if (= first-repeat %2) (reduced %1) (inc %1)) 0 seen)]
    [(subvec seen start) (count seen)]))
    
(resource-value (nth (first repeating-pattern) (mod (- number-of-minutes (second repeating-pattern)) (count (first repeating-pattern)))))

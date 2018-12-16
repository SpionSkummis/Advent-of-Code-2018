(def day11input 7165)

;; Calculate power level :: int -> int -> int -> int
(defn power-level [x y serial]
  (let [rack-id (+ x 10)
        power-level (* rack-id (+ serial (* y rack-id)))]
    (- (quot (mod power-level 1000) 100) 5)))

;; Hash-map representing a 300x300 grid of power-levels
(def grid
  (apply merge
   (for [x (range 1 301)
         y (range 1 301)]
     {[x y] (power-level x y day11input)})))

;; Day 11-1

;; Calculates power of the square with upper-left corner x,y and size size :: int -> int -> int -> int 
(defn power-by-size
  ([x y size] (power-by-size x y size size))
  ([x y x-size y-size]
   (->> (for [x (range x (+ x x-size))
              y (range y (+ y y-size))]
          (grid [x y]))
        (reduce +))))

(->> (for [x (range 1 299)
           y (range 1 299)]
       [(power-by-size x y 3) [x y]])
     (reduce #(if (> (first %1) (first %2)) %1 %2))
     second)

;; Day 11-2

;; Hash-map representing a 300x300 grid of the summed power levels of the rectangle where [x y] is the lower right corner
(def summed-areas
  (loop [x 1 y 1 areas {}]
    (when (= 1 x y) (println y))
    (if (> y 300)
      areas
      (let [new-value
            (if (= 1 x y) (grid [x y])
                (if (= 1 x)
                  (+ (grid [x y]) (get-in areas [(str x) (str (dec y))]))
                  (if (= 1 y)
                    (+ (grid [x y]) (get-in areas [(str (dec x)) (str y)]))
                    (- (+ (grid [x y])
                          (get-in areas [(str x) (str (dec y))])
                          (get-in areas [(str (dec x)) (str y)]))
                       (get-in areas [(str (dec x)) (str (dec y))])))))]
        (recur (if (> x 299) (- x 299) (inc x))
               (if (> x 299) (inc y) y)
               (assoc-in areas [(str x) (str y)] new-value))))))

(loop [x 1 y 1 size 1 biggest-yet [0 [0 0] 0]]
  ;; If we've checked every size up to 300, we're done
  (if (> size 300)
    biggest-yet
    ;; Otherwise calculate the power level of the square with upper left corner [x y] and side length size
    (let [area
        (if (= x y 1) (get-in summed-areas [(str (dec (+ x size))) (str (dec (+ y size)))])
            (if (= 1 x)
              (- (get-in summed-areas [(str (dec (+ x size))) (str (dec (+ y size)))])
                 (get-in summed-areas [(str (dec (+ x size))) (str (dec y))]))
              (if (= 1 y)
                (- (get-in summed-areas [(str (dec (+ x size))) (str (dec (+ y size)))])
                   (get-in summed-areas [(str (dec x)) (str (dec (+ y size)))]))
                (- (+ (get-in summed-areas [(str (dec (+ x size))) (str (dec (+ y size)))])
                      (get-in summed-areas [(str (dec x)) (str (dec y))]))
                   (get-in summed-areas [(str (dec x)) (str (dec (+ y size)))])
                   (get-in summed-areas [(str (dec (+ x size))) (str (dec y))])))))]
      (recur (if (> (+ x size) 300) 1 (inc x))
             (if (and (> (+ y size) 300) (> (+ x size) 300)) 1 (if (> (+ x size) 300) (inc y) y))
             (if (and (> (+ y size) 300) (> (+ x size) 300)) (+ 1 size) size)
             (if (> area (first biggest-yet)) [area [x y] size] biggest-yet)))))

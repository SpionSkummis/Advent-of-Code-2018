(def initial-state (loop [x 0 y 0 found {:corners [] :carts [] :intersections []} remaining (apply list (slurp "./day13input.txt"))]
  (if (some? (peek remaining))
    (let [current (peek remaining)
          newly-found (if (= current \+)
                        (assoc found :intersections (conj (found :intersections) [x y]))
                        (if (= current \\)
                          (assoc found :corners (conj (found :corners) {:pos [x y] :type :up-right}))
                          (if (= current \/)
                            (assoc found :corners (conj (found :corners) {:pos [x y] :type :up-left}))
                            (if (= current \<)
                              (assoc found :carts (conj (found :carts) {:pos [x y] :vel [-1 0] :turn :left}))
                              (if (= current \>)
                                (assoc found :carts (conj (found :carts) {:pos [x y] :vel [1 0] :turn :left}))
                                (if (= current \^)
                                  (assoc found :carts (conj (found :carts) {:pos [x y] :vel [0 -1] :turn :left}))
                                  (if (= current \v)
                                    (assoc found :carts (conj (found :carts) {:pos [x y] :vel [0 1] :turn :left}))
                                    found)))))))]
      (recur (if (= current \newline) 0 (inc x))
             (if (= current \newline) (inc y) y)
             newly-found
             (pop remaining)))
    found)))

;; Rotation matrices. Note that :right and :left are inverted since y is positive downwards.
(def turn-matrices {:right [[0 -1] [1 0]] :left [[0 1] [-1 0]] :up-left [[0 -1] [-1 0]] :up-right [[0 1] [1 0]] :straight [[1 0] [0 1]]})

;; Given current turn type, returns the next :: key -> key
(defn next-turn [current] (some {:left :straight :straight :right :right :left} [current]))
 
;; Function for adding two two-element vectors :: [int int] -> [int int] -> [int int]
(defn vec-add [[x1 y1] [x2 y2]] [(+ x1 x2) (+ y1 y2)])

;; Returns new velocity given old velocity and which way the cart turns :: [int int] -> key -> [int int]
(defn turn [vel turn-type]
  (let [matrix (turn-matrices turn-type)]
    [(+ (* (first (first matrix)) (first vel)) (* (second (first matrix)) (second vel)))
     (+ (* (first (second matrix)) (first vel)) (* (second (second matrix)) (second vel)))]))

;; Functions for checking if a coord is a corner or an intersection, respectively :: [int int] -> bool/nil
(defn corner? [pos] (some #(= pos %) (map :pos (initial-state :corners))))
(defn intersection? [pos] (some #(= pos %) (initial-state :intersections)))

;; Returns true if some cart in carts har :pos pos :: [int int] -> {carts} -> bool/nil
(defn cart-at? [pos carts] (some #(= pos %) (map :pos carts)))

;; Takes a cart and the list of carts. Returns a cart in the next position :: {:pos [int int], :vel [int int], :turn key} -> {:pos [int int], :vel [int int], :turn key} 
(defn move [cart]
  (let [new-pos (vec-add (cart :pos) (cart :vel))
        new-vel (if (corner? new-pos)
                    (some #(when (= new-pos (% :pos)) (turn (cart :vel) (% :type)))
                                 (initial-state :corners))
                    (if (intersection? new-pos)
                      (turn (cart :vel) (cart :turn)) (cart :vel)))
        new-turn-type (if (intersection? new-pos) (next-turn (cart :turn)) (cart :turn))]
    {:pos new-pos
     :vel new-vel
     :turn new-turn-type}))

;; Day 13-1
;; Move all of the carts and flag any ones that collide :: [{cart} ...] -> [{cart} ...]
(defn tick-1 [carts]
  (loop [remaining (vec (reverse (sort-by #(second (% :pos)) (sort-by #(first (% :pos)) carts)))) moved []]
    (if (empty? remaining)
      moved
      (let [current (move (peek remaining))]
        (recur (pop remaining)
               (conj moved (if (cart-at? (current :pos) (concat moved remaining)) (assoc current :crash true) current)))))))

(loop [carts (initial-state :carts)]
  ;; If some cart is flagged as crashed, return its position. Otherwise, do another tick
  (if (some #(contains? % :crash) carts)
    (some #(when (contains? % :crash) (% :pos)) carts)
    (recur (tick-1 carts))))

;; Day 13-2
;; Move all of the carts and remove any ones that collide :: [{cart} ...] -> [{cart} ...]
(defn tick-2 [carts]
  (loop [remaining (vec (reverse (sort-by #(second (% :pos)) (sort-by #(first (% :pos)) carts)))) moved []]
    (if (empty? remaining)
      moved
      (let [current (move (peek remaining))]
        (recur (if (cart-at? (current :pos) (pop remaining))
                 (vec (remove #(= (current :pos) (% :pos)) (pop remaining)))
                 (pop remaining))
               (if (cart-at? (current :pos) (concat moved (pop remaining)))
                 (remove #(= (current :pos) (% :pos)) moved)
                 (conj moved current)))))))

(loop [carts (initial-state :carts)]
  ;; If only one cart left, return its position
  (if (= 1 (count carts))
    ((first carts) :pos)
    (recur (tick-2 carts))))

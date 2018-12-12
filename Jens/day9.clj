(defn add-to-circle
  [circle position number]
  (concat
   (take position circle)
   [number]
   (drop position circle)))

(defn remove-from-circle [circle position]
  (concat
   (take position circle)
   (drop (inc position) circle)))

(defn play-game [number-of-players last-score]
  (loop [i 1 active 0 circle [0] player-scores (repeat number-of-players 0)]
    (println (str "Marble: " i "\nActive: " active "\nCircle: " (apply str (map str circle (repeat " ")))))
    (if (= 1 i)
      (recur (inc i) 1 [0 1] player-scores)
      (if (= 0 (mod i 23))
        (let [current-player (mod i number-of-players)
              seven-prior (mod (- active 7) (count circle))
              marble-score (+ i (nth circle seven-prior))
              new-scores (concat
                          (take current-player player-scores)
                          [(+ marble-score (nth player-scores current-player))]
                          (drop (inc current-player) player-scores))]
          (println "Score! " marble-score)
          (if (= marble-score last-score)
            (apply max new-scores)
            (recur (inc i) seven-prior (remove-from-circle circle seven-prior) new-scores)))
        (let [marble-position (mod (+ 2 active) (count circle))]
          (recur (inc i) marble-position (add-to-circle circle marble-position i) player-scores))))))

;; Positive integers shifts circle CCW :: int -> [int ...] -> [int ...]
(defn shift [steps circle]
  (if (< steps 0)
    (into [] (concat (subvec circle (+ steps (count circle))) (subvec circle 0 (+ steps (count circle)))))
    (into [] (concat (subvec circle steps) (subvec circle 0 steps)))))

(defn play-game [number-of-players last-score]
  (loop [i 2 circle [1 0] player-scores (repeat number-of-players 0)]
    (when (= 0 (mod i 1000)) (println i))
    (if (< last-score i)
      (apply max player-scores)
      (if (= 0 (mod i 23))
        (let [current-player (mod i number-of-players)
              marble-score (+ i (first (shift -9 circle)))
              new-scores (concat
                          (take current-player player-scores)
                          [(+ marble-score (nth player-scores current-player))]
                          (drop (inc current-player) player-scores))]
          (recur (inc i) (into [] (shift 2 (into [] (drop 1 (shift -9 circle))))) new-scores))
        (recur (inc i) (into [] (shift 1 (conj circle i))) player-scores)))))

(defn get-marble [number prev next] {:number number :prev prev :next next})

(defn place-marble [circle number after]
  (let [next-marble ((circle after) :next)]
    (merge circle
           {number (get-marble number after next-marble)}
           {after (get-marble after ((circle after) :prev) number)}
           {next-marble (get-marble next-marble number ((circle next-marble) :next))})))

(defn remove-marble [circle number]
  (let [next-marble ((circle number) :next)
        prev-marble ((circle number) :prev)]
    (merge (dissoc circle number)
           {next-marble (get-marble next-marble prev-marble ((circle next-marble) :next))}
           {prev-marble (get-marble prev-marble ((circle prev-marble) :prev) next-marble)})))
  

(defn n-prev [circle active n]
  (loop [i n a active]
    (if (= 0 i)
      (circle a)
      (recur (dec i) ((circle a) :prev)))))

(defn play-game [number-of-players last-marble]
  (loop [i 2 active 1 circle {0 {:number 0 :prev 1 :next 1} 1 {:number 1 :prev 0 :next 0}} player-scores (apply assoc {} (interleave (range 0 number-of-players) (repeat number-of-players 0)))]
    (when (= 0 (mod i 100000)) (println i))
    (if (> i last-marble)
      (apply max (vals player-scores))
      (if (= 0 (mod i 23))
        (let [seven-prior ((n-prev circle active 7) :number)
              marble-score (+ i seven-prior)]
          (recur
           (inc i)
           ((circle seven-prior) :next)
           (remove-marble circle seven-prior)
           (update player-scores (mod i number-of-players) + marble-score)))
        (recur
         (inc i)
         i
         (place-marble circle i ((circle active) :next))
         player-scores)))))

;; Day 9-1
(play-game 470 72170)

;; Day 9-2
(play-game 470 7217000)

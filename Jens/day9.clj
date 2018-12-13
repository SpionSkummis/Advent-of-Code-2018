;; "Create" a marble, a hash-map containing info about the marble's own number and between which marbles it is placed
(defn get-marble [number prev next] {:number number :prev prev :next next})

;; Add a marble numbered 'number' to the hash-map 'circle' after the marble numbered 'after' and update the marbles on either side
(defn place-marble [circle number after]
  (let [next-marble ((circle after) :next)]
    (merge circle
           {number (get-marble number after next-marble)}
           {after (get-marble after ((circle after) :prev) number)}
           {next-marble (get-marble next-marble number ((circle next-marble) :next))})))

;; Remove the marble numbered 'number' and update the marbles on either side
(defn remove-marble [circle number]
  (let [next-marble ((circle number) :next)
        prev-marble ((circle number) :prev)]
    (merge (dissoc circle number)
           {next-marble (get-marble next-marble prev-marble ((circle next-marble) :next))}
           {prev-marble (get-marble prev-marble ((circle prev-marble) :prev) next-marble)})))
  
;; Return the number of the marble 'n' positions before the marble numbered 'active', in hash-map 'circle'
(defn n-prev [circle active n]
  (loop [i n a active]
    (if (= 0 i)
      (circle a)
      (recur (dec i) ((circle a) :prev)))))

;; Play a game of 'number-of-players' players and place 'last-marble' marbles. Return winning score.
(defn play-game [number-of-players last-marble]
  ;; Start with marble number 2 and a circle containing marbles 0 and 1, to avoid edge cases
  (loop [i 2 active 1 circle {0 {:number 0 :prev 1 :next 1} 1 {:number 1 :prev 0 :next 0}} player-scores (apply assoc {} (interleave (range 0 number-of-players) (repeat number-of-players 0)))]
    ;; If we're done, return the winning score
    (if (> i last-marble)
      (apply max (vals player-scores))
      (if (= 0 (mod i 23))
        ;; i is divisible by 23
        (let [seven-prior ((n-prev circle active 7) :number) ; Number of marble to remove
              marble-score (+ i seven-prior)] ; The amount of points scored by the player
          (recur
           (inc i) ; Next marble
           ((circle seven-prior) :next) ; The marble after the removed one is set as active
           (remove-marble circle seven-prior) ; Remove the marble from the circle
           (update player-scores (mod i number-of-players) + marble-score))) ; Update scores
        (recur
         (inc i) ; Next marble
         i ; Current marble set as active
         (place-marble circle i ((circle active) :next)) ; Add current marble to circle
         player-scores))))) ; Do nothing with the scores

;; Day 9-1
(play-game 470 72170)

;; Day 9-2
(play-game 470 7217000)

;; Reads input into list :: ([before after] ...)
(def day7input (map (partial drop 1) (re-seq #"Step\s([A-Z]).*([A-Z]).*\n" (slurp "./day7input.txt"))))

;; Day 7-1
(def sorted-alphabet (map #(str (char %)) (range (int \A) (inc (int \Z)))))

(defn find-children [node coll]
  (map second (filter #(= (first %) node) coll)))

(defn find-parents [node coll]
  (map first (filter #(= (second %) node) coll)))

(def parent-list
  (->> day7input
       (map #(vector (first %) (find-parents (first %) day7input)))
       distinct
       (remove #(= 0 (count (second %))))))

(def starting-nodes
  (->> parents
       (filter #(= 0 (count (second %))))
       (map first)
       sort
       (apply list)))

(def all-but-the-last
  (loop [used [] unresolved starting-nodes remaining parent-list]
    (if (= nil (peek unresolved))
      used
      (let [current (peek unresolved)
            this-step (map (fn [x] (vector (first x) (remove #(= current %) (second x)))) remaining)]
        (recur
         (conj used current)
         (apply list (sort (distinct (concat (pop unresolved) (map first (filter #(= 0 (count (second %))) this-step))))))
         (remove #(= 0 (count (second %))) this-step))))))

(apply str (conj all-but-the-last (first (find-children (peek all-but-the-last) day7input))))

;; Reads input into list :: ([before after] ...)
(def day7input (map (partial drop 1) (re-seq #"Step\s([A-Z]).*([A-Z]).*\n" (slurp "./day7input.txt"))))

;; Returns true if the supplied node has no remaining parent :: [str list] -> bool
(defn parentless? [x] (if (empty? (second x)) true false))

;; Returns all children in coll of node :: str -> ((str str) ...) -> (str ...)
(defn find-children [node coll]
  (map second (filter #(= (first %) node) coll)))

;; Returns all parents in coll of node :: str -> ((str str) ...) -> (str ...)
(defn find-parents [node coll]
  (map first (filter #(= (second %) node) coll)))

;; The entire input on the form ([child (parents)] ...) :: ([str (str ...)] ...)
(def parent-list
  (distinct
   (concat
    (map #(vector (second %) (find-parents (second %) day7input)) day7input)
    (map #(vector (first %) (find-parents (first %) day7input)) day7input))))

;; Nodes with no parents :: (str ...)
(def starting-nodes
  (->> parent-list
       (filter parentless?)
       (map first)
       sort
       (apply list)))

;; Removes every reference to p (as parent) in coll 
(defn remove-parent [p coll]
  (map (fn [x] (vector (first x) (remove #(= p %) (second x)))) coll))

;; Day 7-1

(apply str
       (loop [used [] unresolved starting-nodes remaining (remove parentless? parent-list)]
         (if (= nil (peek unresolved))
           used
           (let [current (peek unresolved)
                 this-step (remove-parent current remaining)]
             (recur
              (conj used current) ; Add current node to vector of passed nodes
              (apply list (sort (distinct (concat (pop unresolved) (map first (filter parentless? this-step)))))) ; Add every node which no longer has any parents to the list of nodes to parse
              (remove parentless? this-step)))))) ; Remove those nodes from the list of nodes

;; Day 7-2

;; Calculate time needed to finish a job :: str -> int
(defn time-needed [job] (+ 60 (- (int (char (first job))) (int \A))))

;; Take worker id:s as vector and return hash-map of workers with assigned jobs:: [int ...] -> '(str ...) -> int -> {id {:finished :job}}
(defn assign-workers [workers jobs current-second]
  (let [max-it (min (count workers) (count jobs)) worker-vec (vec workers)]
    (loop [i 0 newly-assigned {}]
      (if (= max-it i)
        newly-assigned
        (recur (inc i) (assoc newly-assigned (nth worker-vec i) {:finished (+ current-second (time-needed (nth jobs i))) :job (nth jobs i)}))))))

(loop [current-second 1
       workers {0 {:finished 0 :job nil} 1 {:finished 0 :job nil} 2 {:finished 0 :job nil} 3 {:finished 0 :job nil} 4 {:finished 0 :job nil}}
       unresolved starting-nodes
       remaining (vec (remove parentless? parent-list))]
  ;; No input left and no busy workers means we're finished
  (if (and (empty? remaining) (empty? unresolved) (every? #(>= current-second (:finished (second %))) workers))
    current-second
    (let [free-workers (mapv first (filter #(>= current-second (:finished (second %))) workers))
          finished-jobs (mapv #(:job (workers %)) free-workers)
          newly-assigned (assign-workers free-workers unresolved current-second)
          updated-workers (merge workers newly-assigned)
          currently-remaining (vec (loop [jobs finished-jobs r remaining] (if (seq jobs) (recur (pop jobs) (remove-parent (peek jobs) r)) r)))
          parentless (mapv first (filter parentless? currently-remaining))
          new-unresolved (apply list (sort (vec (concat (loop [i (count newly-assigned) u unresolved] (if (> i 0) (recur (dec i) (pop u)) u)) parentless))))]
      (recur (inc current-second)
             updated-workers
             new-unresolved
             (vec (remove parentless? currently-remaining))))))


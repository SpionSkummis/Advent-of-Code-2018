;; Read input to list :: '(int ...)
(def day8input (vec (map read-string (clojure.string/split (slurp "./day8input.txt") #"\s+"))))

;; Day 8-1

;; Take input and return a vector describing the first node found without children [start end data] :: [int ...] -> [int int int]
(defn first-bottom-node [input]
  (loop [branches (take-nth 2 input) index 0]
    (if (= 0 (first branches))
      (let [found (* 2 index)
            end (+ 2 found (nth input (inc found)))]
        (vector found end (apply + (subvec input (+ 2 found) end))))
      (recur (drop 1 branches) (inc index)))))

;; Take a node description and input and return input with the described node removed :: [int int int] -> [int ...] -> [int ...]
(defn remove-node [node-desc input]
  (vec (concat (subvec input 0 (first node-desc)) (subvec input (second node-desc)))))

(loop [input day8input total 0]
  ;; To avoid edge cases, jump to output as soon as there is only one node remaining in input
  (if (> (+ 3 (second input)) (count input))
    (+ total (apply + (subvec input 2))) ; Output total plus metadata of final node
    (let [node (first-bottom-node input) ; First bottom node
          new-tree (assoc (remove-node node input) ; Input with node removed
                          (- (first node) 2) (dec (nth input (- (first node) 2))))] ; Decrease number of children for parent node
      (recur new-tree (+ total (peek node))))))

;; Day 8-2

;; Take a node description and input and replace the described node with a vector containing its value :: [int int int] -> [int ...] -> [int ... [int] int ...]
(defn collapse-node [node-desc input]
  (vec (concat (conj (subvec input 0 (first node-desc)) [(last node-desc)]) (subvec input (second node-desc)))))

;; Sum the value of a node, if sub-branches and meta-data is known :: [int ...] -> [int ...] -> int
(defn sum-node [sub-branches meta-data]
  #dbg (if (empty? sub-branches)
    (reduce + meta-data)
    (reduce + (flatten (map #(nth sub-branches (dec %) 0) meta-data)))))

;; Find the first node that can be fully solved and return a description of it :: [int ...] -> [int int int]
(defn first-solvable-node [input]
  (loop [branches input distance 0 index 0]
    (if (= 0 (first branches) (mod distance 2))
    #dbg  (let [found index
            sub-branches (loop [i 0 result []]
                           (if (vector? (nth input (+ found 2 i)))
                             (recur (inc i) (conj result (nth input (+ found 2 i))))
                             result))
            meta-data (subvec input (+ 2 found (count sub-branches)) (+ 2 found (count sub-branches) (nth input (inc found))))
            end (+ 2 found (count sub-branches) (count meta-data))]
        (vector found end (sum-node sub-branches meta-data)))
      (recur (drop 1 branches) (if (vector? (first branches)) 0 (inc distance)) (inc index)))))

(loop [input day8input top-branches (first day8input)]
  ;; To avoid edge cases, jump to output as soon as there is only one node remaining in input
  (if (> (+ 3 top-branches (second input)) (count input))
    (+ (sum-node (subvec 2 (+ 2 top-branches)) (subvec (+ 2 top-branches))))
    (let [node (first-solvable-node input)
          new-tree (assoc (collapse-node node input)
                          (- (first node) 2) (dec (nth input (- (first node) 2))))]
      (recur new-tree top-branches))))

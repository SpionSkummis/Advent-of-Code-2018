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
;; Return number of vectors in the branch :: [int/[int] ...] -> int
(defn count-sub-branches [branch]
  (reduce #(if (vector? %2) (inc %1) %1) 0 (subvec branch 2)))

;; Sum the node in input found between start (inclusive) and end (exclusive) :: [int/[int] ...] -> [int int] -> int
(defn sum-node [input [start end]]
  (let [node (subvec input start end)]
    (if (= 0 (first node))
      ;; No sub-branches, sum metadata
      (reduce + (subvec node 2))
      ;; Branches, read metadata and sum branch values
      (let [branch-data (flatten (subvec node 2 (+ 2 (first node)))) ; Vector of branch values
            meta-data (subvec node (+ 2 (first node)))] ; Metadata
        ;; For each metadata, pick corresponding branch value. Sum them all.
        (reduce + (map #(nth branch-data (dec %) 0) meta-data))))))

;; Collapse the node in input found between start (inclusive) and end (exclusive), replacing it with a vector containing its value. :: [int/[int] ...] -> [int int] -> [int/[int] ...]
(defn collapse-node [input [start end]]
  (into (conj (subvec input 0 start) [(sum-node input [start end])]) (subvec input end)))

;; Find the first node that can be fully solved and returns its start and end index :: [int ...] -> [int int]
(defn first-solvable-node [input]
  (loop [tree input index 0]
    ;; Neither the first nor the second number can be a vector (i.e. calculated sub-branch)
    (if (and (not (vector? (first tree))) (not (vector? (second tree))))
      (if (or (= 0 (first tree)) ; 0 means we've found a top node
              (= (count-sub-branches (subvec tree 0 (+ 2 (first tree)))) (first tree))) ; All sub-branches are calculated
        [index (+ 2 index (first tree) (second tree))] ; [start end]
        (recur (subvec tree 1) (inc index)))
      (recur (subvec tree 1) (inc index)))))

(loop [input day8input]
  (if (= (count input) (+ 2 (first input) (second input)))
    (sum-node input [0 (count input)])
    (recur (collapse-node input (first-solvable-node input)))))

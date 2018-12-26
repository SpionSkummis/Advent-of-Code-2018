;;; INPUT
(def day16input (slurp "./day16input.txt"))

;; Parsing the first part of the input
(def input1
  (vector
   (mapv #(mapv read-string %) (map (partial drop 1) (re-seq #"Before\: \[(\d)\, (\d)\, (\d)\, (\d)" day16input)))
   (mapv #(mapv read-string %) (map (partial drop 1) (re-seq #"\]\n(\d+) (\d) (\d) (\d)" day16input)))
   (mapv #(mapv read-string %) (map (partial drop 1) (re-seq #"After\: +\[(\d)\, (\d)\, (\d)\, (\d)" day16input)))))

;; Parsing the second part of the input
(def input2
  (apply list (map #(map read-string %) (map (partial drop 1) (re-seq #"\n(\d+) (\d) (\d) (\d)(?!\nA)" day16input)))))

;; Record for test cases
(defrecord test-case [before instruction after])

;; Making test cases out of the input
(def test-cases (map ->test-case (first input1) (second input1) (nth input1 2)))

;;; HELPER FUNCTIONS
;; Equality that returns 1 or 0 instead of boolean :: int -> int -> int
(defn eq [a b] (if (= a b) 1 0))

;; Greater than that returns 1 or 0 instead of boolean :: int -> int -> int
(defn gt [a b] (if (> a b) 1 0))

;; Takes two values and returns the first :: a -> b -> a
(defn ret-a [a b] a)

;; Applies f to value(s) in register(s) specified by reg-a and reg-b. Stores result in reg-c.
;; rr-function :: fn -> [int int int int] -> [int int int int] -> [int int int int]
(defn rr-function [f registers [opcode reg-a reg-b reg-c]]
  (vec (for [i (range 0 4)]
         (if (= reg-c i)
           (f (nth registers reg-a) (nth registers reg-b))
           (nth registers i)))))

;; Applies f to value in register specified by reg-a and value val-b. Stores result in reg-c.
;; ri-function :: fn -> [int int int int] -> [int int int int] -> [int int int int] 
(defn ri-function [f registers [opcode reg-a val-b reg-c]]
  (vec (for [i (range 0 4)]
         (if (= reg-c i)
           (f (nth registers reg-a) val-b)
           (nth registers i)))))

;; Applies f to value val-a and value in register specified by reg-b. Stores result in reg-c.
;; ir-function :: fn -> [int int int int] -> [int int int int] -> [int int int int] 
(defn ir-function [f registers [opcode val-a reg-b reg-c]]
  (vec (for [i (range 0 4)]
         (if (= reg-c i)
           (f val-a (nth registers reg-b))
           (nth registers i)))))

;; All of the possible functions :: [int int int int] -> [int int int int] -> [int int int int]
(def addr #(rr-function + %1 %2))
(def addi #(ri-function + %1 %2))
(def mulr #(rr-function * %1 %2))
(def muli #(ri-function * %1 %2))
(def banr #(rr-function bit-and %1 %2))
(def bani #(ri-function bit-and %1 %2))
(def borr #(rr-function bit-or %1 %2))
(def bori #(ri-function bit-or %1 %2))
(def setr #(rr-function ret-a %1 %2))
(def seti #(ir-function ret-a %1 %2))
(def gtir #(ir-function gt %1 %2))
(def gtri #(ri-function gt %1 %2))
(def gtrr #(rr-function gt %1 %2))
(def eqir #(ir-function eq %1 %2))
(def eqri #(ri-function eq %1 %2))
(def eqrr #(rr-function eq %1 %2))

;; All of the functions the device can apply
(def all-functions [addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr])

;; Tests function f with test-case t and returns true if output and :after matches
;; possible-opcode? :: fn -> test-case -> bool
(defn possible-opcode? [f t] (= (:after t) (f (:before t) (:instruction t))))

;; Takes a test case, returns opcode and matching functions :: test-case -> ([int fn] ...)
(defn matching-functions [x]
  (filter some?
          (map #(if (possible-opcode? %1 %2)
                  (vector (first (:instruction %2)) %1)
                  nil)
               all-functions (repeat x))))
;;; DAY 16-1
(count (filter #(>= % 3) (map #(count (matching-functions %)) test-cases)))

;;; DAY 16-2

;; If all opcode-function pairs in the supplied vector are equal, returns that pair. Otherwise, returns nil.
;; unambiguous? :: [[int fn] ...] -> bool
(defn unambiguous? [code-fn-pairs] (reduce #(if (= %1 %2) %1 nil) code-fn-pairs))

;; Matches each opcode to a function in a hash-map, assuming no ambiguous opcodes exist :: {int fn, ...}
(def opcodes
  (loop [remaining (mapcat matching-functions test-cases) solved {}]
  (if (empty? remaining)
    solved
    (let [currently-solved (reduce #(when (some? %2) (reduced %2)) ; Returns the first encountered opcode-function pair
                                   nil ; Starting value for reduce (could be anything)
                                   (map (comp unambiguous? val) (group-by first remaining)))] ; Get unambiguous opcode-pair combinations
      (recur (remove #(= (second %) (second currently-solved)) remaining) ; Remove any pairs containing the solved function
             (assoc solved (first currently-solved) (second currently-solved))))))) ; Add an opcode-function pair to the map

(loop [remaining input2 registers [0 0 0 0]]
  (if (empty? remaining) ; We're done when no instructions remain
    registers ; Return the values of the registers
    (let [instruction (peek remaining)] ; The instruction to execute
      (recur (pop remaining) ; Remaining instructions
             ((opcodes (first instruction)) registers (vec instruction)))))) ; Apply first instruction to registers




















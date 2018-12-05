(require '[clojure.string :as s])

;; Read input into av list of chars :: (char ...)
(def day5input (drop-last 1 (slurp "./day5input.txt")))

;; Checks whether chars a and b are upper and lower case versions of the same char :: char -> char -> boolean
(defn reaction? [a b]
	(if (some? a)
		(and (= (s/lower-case a) (s/lower-case b)) (not= a b))
		false))

;; Reduces string x char by char using reaction? :: (char ...) -> (char ...)
(defn collapse-string [x]
	(reduce (fn [a b]
		(if (reaction? (peek a) b)
			(pop a)
			(conj a b)
		)) [] x))

;; Day 5-1
(count collapse-string day5input)

;; Day 5-2
(apply min (for [i (range (int \A) (int \Z))]
		(count (collapse-string (remove #(= (str (char i)) (s/upper-case %)) day5input)))))

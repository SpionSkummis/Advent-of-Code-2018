;; DAY 1

;; Convert input to list of ints
(def day1input (map read-string (clojure.string/split (slurp "./day1input.txt") #"\n")))

;; Day 1-1
(reduce + day1input)

;; Day 1-2
(loop
	[start 0
	already-used [0]]
	(let
		[new-freqs (reductions + (cons (+ start (first day1input)) (drop 1 day1input)))]
		;; If there are no common numbers between new-freqs and already-used, recur with new-freqs added to already-used
		(if (empty? (clojure.set/intersection (into #{} already-used) (into #{} new-freqs)))
			(recur (last new-freqs) (concat already-used new-freqs))
			(->> new-freqs
				;; Find all common numbers between new-freqs and already-used
				(map (fn [x] (some #(when (= x %) %) already-used)))
				;; Grab the first one
				(reduce #(if (not= nil %1) %1 %2))))))

;; DAY 2

;; Read input into list of strings
(def day2input (clojure.string/split (slurp "./day2input.txt") #"\n"))

;; Day 2-1
(->> day2input
	;; Sort strings alphabetically and split to lists of characters groups of 2 or more characters
	(map #(apply str (sort %)))
	(map (partial re-seq #"(.)\1+"))
	(map (partial map first))
	;; Create a list of vectors on the form [t d] where t and d are 1 or 0 depending on if the string contains triplets or duplicates, respectively
	(map (partial map count))
	(map #(vector (if (some (partial = 3) %) 1 0) (if (some (partial = 2) %) 1 0)))
	;; Sum all t:s and all d:s and multiply the results
	(reduce #(vector (+ (first %1) (first %2)) (+ (second %1) (second %2))))
	(reduce *))

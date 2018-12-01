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

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

;;Day 2-2
(loop
	[remove 0]
	(let
		[current-strings (->>
			;; Remove the nth character
			(if (= 0 remove)
				(map #(subs % 1) day2input)
				(map #(str (subs % 0 remove) (subs % (+ 1 remove))) day2input))
			;; Sort list by number of occurences of each string
			frequencies
			clojure.set/map-invert)]
		;; Find duplicate and output it, or recur increasing remove by 1
		(if (contains? current-strings 2)
			(current-strings 2)
			(recur (inc remove)))))

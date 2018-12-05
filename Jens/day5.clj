;; Read input into av list of chars :: (char ...)
(def day5input (drop-last 1 (slurp "./day5input.txt")))

;; Day 5-1
(def character-offset (Math/abs (- (int \a) (int \A))))

(->> day5input
	; Convert each char to an int :: (char ...) -> (int ...)
	(map int)
	; Compare each int with the last. If the difference matches character offset, remove both. :: (int ...) -> [int ...]
	(reduce #(if (= character-offset (Math/abs (- (last %1) %2)))
		; Drop last int from vector and compare with next
		(into [] (drop-last 1 %1))
		; Add current int to vector and compare with next
		(into [] (conj %1 %2)))
		[0])
	; Remove the leading zero and count (int ...) -> int
	(drop 1)
	count)

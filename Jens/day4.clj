;; Reads input to a list of vectors on the form [month day hour minute event]
(def day4input (mapv (partial drop 1) (map first (map (partial re-seq #"\d+\-(\d+)-(\d+)\s(\d+)\:(\d+)\]\s(.+)") (clojure.string/split (slurp "./day4input.txt") #"\n")))))

;; Day 4-1
(def formatted-input (->> (sort-by (juxt first second #(nth % 2) #(nth % 3)) day4input)
		;; If an id is present in the event string, it means a new night has started
		(map #(if (not= 0 (count (re-find #"\d+" (nth % 4))))
				;; New night, output [elf-id 0].
				(vector (read-string (str "10r" (re-find #"\d+" (nth % 4)))) 0)
				;; Same night, output [nil minutes-past-midnight]
				(vector nil (read-string (str "10r" (nth % 3))))))
		;; Reduce each night to one vector [elf-id 0 fell-asleep woke-up (etc.)]	
		(reduce #(if (some? (first %2))
			(conj %1 %2)
			(conj (into [] (drop-last 1 %1)) (conj (last %1) (second %2))))
			[])))

(let
	[sleepiest (->> formatted-input
		;; For each night, sum every wake-up timestamp and subtract every fall-asleep timestamp to get number of minutes slept per night
		(map #(vector (first %) (- (reduce + (take-nth 2 (drop 1 %))) (reduce + (take-nth 2 (drop 2 %))))))
		;; Group by elf-id and sum total minutes slept
		(group-by first)
		(map (fn [x] (concat (vector (first x)) (reduce #(vector (+ (first %1) (first %2))) (map (partial drop 1) (second x))))))
		;; Find the sleepiest
		(reduce #(if (> (second %1) (second %2)) %1 %2))
		first)
	most-slept-minute (->> (filter #(= sleepiest (first %)) formatted-input)
		;; Get ranges of minutes slept each night
		(map #(map range (take-nth 2 (drop 2 %)) (take-nth 2 (drop 3 %))))
		;; Find the most frequent
		flatten
		frequencies
		(reduce #(if (> (second %1) (second %2)) %1 %2))
		first)]
	(* sleepiest most-slept-minute)
)

;; Day 4-2
(let [answer (->> formatted-input
		;; Get pairs [elf-id minute] for each minute slept
		(map #(map vector (repeat (first %)) (flatten (map range (take-nth 2 (drop 2 %)) (take-nth 2 (drop 3 %))))))
		(reduce concat)
		;; Sort by frequency
		frequencies
		(sort-by second)
		;; Grab the first one and multiply elf-id by minute
		last
		first
		(reduce *)
	)]
	answer
)

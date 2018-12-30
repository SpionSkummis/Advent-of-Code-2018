#pragma once
#include "timeDate.h"
#include <algorithm>
#include <vector>
class guard
{

public:

	vector<int>* minutesAsleep;
	int minutesAsleepTot = 0;
	int ID;
	bool isAsleep = false;

	guard(int ID) {
		this->ID = ID;
		minutesAsleep = new vector<int>(60, 0);
	}
		;
	~guard() {};


	void minutesSleepingGrid(timeDate& start, timeDate& wake) {
		for (int i = start.get_min(); i < wake.get_min(); i++) {
				(minutesAsleep->at(i))++;
				minutesAsleepTot++;
		}
		
		
	}

	
	int mostSleptMinute() {

		
		auto maxElement = max_element(minutesAsleep->begin(), minutesAsleep->end());
		auto it = minutesAsleep->begin();
		int i = 0;

		for (it; it != minutesAsleep->end(); it++) {
			if (it == maxElement) {
				break;
			}
			i++;
		}

		cout << "Guard " << ID << " slept " << *maxElement << " times on minute " << i << endl;

		return i;

	}
	

	bool operator==(const guard &guard2) const {
		return (ID == guard2.ID);
	}

	bool operator<(const guard& guard2) const {
		return (minutesAsleepTot < guard2.minutesAsleepTot);
	}

	void print() const {
		cout << "ID is " << ID << "|| Total minutes asleep: " << minutesAsleepTot << "||  " << endl;
	}
};



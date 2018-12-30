#include "timeDate.h"

class event {

private:
	

public:
	timeDate* time;
	int ID;
	bool isAsleep;


	event(int year, int month, int day, int hour, int min, int ID = 0, bool isAsleep = 0) {
		this->time = new timeDate(year,month,day,hour, min);
		this->isAsleep = isAsleep;
		this->ID = ID;

	}

	bool operator<(const event& event2) const {
		return *time < *event2.time;
	}

	void print() {

		time->print();
		cout << "ID is " << ID << " ***   isAsleep: " << isAsleep << endl << endl;
	}




};

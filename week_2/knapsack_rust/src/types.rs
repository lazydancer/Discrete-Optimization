pub struct Item {
    pub value: i32,
    pub weight: i32,
}

pub struct State {
    pub items: Vec<Item>,
    pub capacity: i32,
}

impl State {
    pub fn total_score(&self, selected: &[bool]) -> i32 {
        let mut result = 0;
        for (i, s) in selected.iter().enumerate() {
            if *s {
                result += self.items[i].value;
            }
        }

        result
    }

    pub fn total_weight(&self, selected: &[bool]) -> i32 {
        let mut result = 0;
        for (i, s) in selected.iter().enumerate() {
            if *s {
                result += self.items[i].weight;
            }
        }

        result
    }

    pub fn upper_bound(&self, selected: &[bool]) -> i32 {
        let score = self.total_score(selected);
        let weight = self.total_weight(selected);

        let remaining_items = self.items[selected.len()..];
        // remaining items
        // sort by value/weight
        // take the value until used up capacity
        4
    }
}

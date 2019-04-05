extern crate rand;
use rand::Rng;

use super::types;

pub fn run(state: &types::State) -> Vec<bool> {
    loop {
        let selected: Vec<bool> = random_selection(state.items.len());
        if state.total_weight(&selected) <= state.capacity {
            let score = state.total_score(&selected);
            if score > 92000 {
                return selected;
            }
        }
    }
}

fn random_selection(size: usize) -> Vec<bool> {
    let mut rng = rand::thread_rng();

    let mut result: Vec<bool> = Vec::new();
    for _ in 0..size {
        let random_bool: bool = rng.gen();
        result.push(random_bool);
    }

    result
}

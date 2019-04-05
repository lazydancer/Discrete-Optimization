extern crate rand;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

mod attempt_random;
mod attempt_tree;
mod types;

fn main() {
    let state = read_file();

    let result: Vec<bool> = attempt_tree::run(&state);

    //let result: Vec<bool> = attempt_random::run(&state);
    create_output(state.total_score(&result), &result);

}

fn read_file() -> types::State {
    let file_loc = "../knapsack/tmp.data";

    let f = File::open(file_loc).unwrap();
    let reader = BufReader::new(&f);

    let mut capacity = 0;
    // Get Items
    let mut items: Vec<types::Item> = Vec::new();
    for (num, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let mut iter = line.split_whitespace();
        if num == 0 {
            let _ = iter.next(); // Value not needed but to next
            capacity = iter.next().unwrap().parse().unwrap();
        } else {
            let value: i32 = iter.next().unwrap().parse().unwrap();
            let weight: i32 = iter.next().unwrap().parse().unwrap();
            items.push(types::Item { value, weight });
        }
    }

    types::State { items, capacity }
}

fn create_output(score: i32, selected: &[bool]) {
   
    let mut result = String::new();

    for s in selected.iter() {
        if *s {
            result.push('1');
        } else {
            result.push('0');
        }
        result.push(' ');
    }

    println!("{} 1", score);
    println!("{}", result);
}

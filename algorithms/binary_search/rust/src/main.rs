use std::io::{self};
use serde::{Deserialize, Serialize};
//use serde_json::{Result, Value};


#[derive(Serialize, Deserialize)]
struct InputArray {
    entries: Vec<u8>,
    target: u8
}

fn binary_search(list: &Vec<u8>, start: usize, end: usize, target: u8) {
    let index = (start + end) / 2;

    println!("start: {}, end: {}", start, end);
    println!("index: {}", index);

    if list[index] == target {
       println!("found target {} at index {}", target, index);
       return;
    }
    else if start == end {
       println!("could not find target {}", target);
       return;
    }
    else if list[index] < target {
        binary_search(list, index + 1, end, target);
    }
    else {
        binary_search(list, start, index - 1, target);
    }
}


fn main() -> io::Result<()> {

    // Read input from stdin
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;

    
    // Extract "entries" array from input json
    let input: InputArray = serde_json::from_str(&buffer)?;

    println!("\n\nTest Input");
    let entries = input.entries;
    println!("entries: {:?}", entries);

    let target = input.target;
    println!("target: {}", target);

    let start_index = 0;
    let end_index = entries.len() - 1;

    println!("Test Start");
    binary_search(&entries, 
                  start_index, 
                  end_index,
                  target);

    println!("Test End");
    
    Ok(())
}


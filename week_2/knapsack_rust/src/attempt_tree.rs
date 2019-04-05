use super::types;

pub fn run(state: &types::State) -> Vec<bool> {

    let mut stack: Vec<bool> = Vec::new();
    let mut from: Option<bool> = None;
    let mut zero_flag: i32 = 0;
    let mut max_value = 0;
    let mut max_input: Vec<bool> = Vec::new();
    
    
    loop {
        if stack.len() == state.items.len() {
            from = stack.pop();
            
        }

        match from {
            Some(true) => {
                stack.push(false);
                from = None;
            },
            Some(false) => {
                from = stack.pop();
            }
            None => { 
                stack.push(true);
                from = None;
            }  
        }


        let over_weight = state.total_weight(&stack) > state.capacity;
        if over_weight {
            from = Some(false);
        }


        if stack.len() == state.items.len() 
            && !over_weight
            && state.total_score(&stack) > max_value 
        {

            max_value = state.total_score(&stack);
            max_input = stack.clone(); 

            //println!("{:?}, {}", max_input, max_value);
        }

        // Have a zero length happens when transfering
        // from left to right and when complete!
        if stack.is_empty() {
            zero_flag += 1;
            if zero_flag == 2 {
                break;
            }
        }
        
   }

   max_input
   
}
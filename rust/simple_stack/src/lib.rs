
#[derive(Debug, PartialEq)]
pub struct Stack{
    data: Vec<i32>,
}

impl  Stack{
    pub fn new() -> Self{
        Stack { data: Vec::new() }
    }

    pub fn push(&mut self, value: i32){
        self.data.push(value);
    }

    pub  fn pop(&mut self) -> Option<i32>{
        self.data.pop()
    }

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new() {
        let manual_stack = Stack { data: Vec::new() };
        let constructed = Stack::new();
        assert_eq!(manual_stack, constructed);
    }

    #[test]
    fn test_push(){
        let mut stack = Stack::new();
        stack.push(41);
        assert_eq!(stack.data, vec![41])
    }

    #[test]
    fn test_pop_return(){
        let  mut stack = Stack::new();
        stack.push(1);
        let stack_pop = stack.pop();


        // The thin here, using Some keyword is because Rust enforce type, because in some
        // cases the result can be None, Some come to solve this issue
        // in the same way that the Option<i32> handles the return type

        let expeceted_value: Option<i32> = Some(1);
       
        assert_eq!(stack_pop, expeceted_value);
    }

    #[test]
    fn test_pop_stack(){
        let  mut stack = Stack::new();
        stack.push(1);
        stack.pop();
       
        assert_eq!(stack, Stack::new());
    }

}



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

    pub fn peek(self) -> Option<i32>{
        // pub fn peek(&mut self) -> Option<&i32>{
        // To return a i32 had to use cloned, otherwise would be like above
        self.data.last().cloned()
    }

    pub fn is_empty(&mut self) -> bool{
        self.data.is_empty()
    }

    pub fn size(&self) -> Option<i32> {
        // The compiler will look into the header of fucntion before apply try into
        self.data.len().try_into().ok()
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

    #[test]
    fn test_peek(){
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);

        let peeked_value = stack.peek();
        assert_eq!(peeked_value, Some(2))
    }

    #[test]
    fn test_is_empty_empty(){
        let mut stack = Stack::new();
        assert_eq!(stack.is_empty(), true)
    }

    #[test]
    fn test_is_empty_filled(){
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert_eq!(stack.is_empty(), false)
    }

    #[test]
    fn test_size(){
        let stack = Stack::new();
        assert_eq!(stack.size(), Some(0))
                
    }

    #[test]
    fn test_size_5(){
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(1);
        stack.push(1);
        stack.push(1);
        stack.push(1);

        assert_eq!(stack.size(), Some(5))
                
    }

    #[test]
    fn test_lifo_behaviour(){
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        
        assert_eq!(stack.pop(), Some(3));
        assert_eq!(stack.pop(), Some(2));
        assert_eq!(stack.pop(), Some(1));
        assert_eq!(stack.pop(), None)
    }
}


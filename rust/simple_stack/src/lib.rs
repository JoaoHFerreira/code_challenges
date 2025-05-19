
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


}


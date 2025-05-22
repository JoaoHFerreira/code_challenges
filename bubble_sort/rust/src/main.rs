
pub fn bubble_sort(mut array: Vec<i32>) -> Vec<i32>{
    let n = array.len();
    for i in 0..n   {
        for j in 0..n -i -1{
            if array[j] > array[j+1] {
                array.swap(j, j+1);
            }
        }
    }
    array
}


#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn test_bubble_sort(){
        let array = bubble_sort(vec![9,4,8,3]);
        assert_eq!(vec![3,4,8,9], bubble_sort(array));
    }
}
fn binary_search(list: &Vec<u8>, start: usize, end: usize, target: u8) -> Option<usize> {
    let index = (start + end) / 2;

    match list[index] {
        item => {
            if item == target {
                Some(index)
            } else if start == end {
                None
            } else if item < target {
                binary_search(list, index + 1, end, target)
            } else {
                binary_search(list, start, index - 1, target)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_binary_search_basic() {
        let entries: Vec<u8> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].to_vec();
        let start_index = 0;
        let end_index = entries.len() - 1;
        let target = 3;
        assert_eq!(
            binary_search(&entries, start_index, end_index, target),
            Some(3)
        )
    }
}

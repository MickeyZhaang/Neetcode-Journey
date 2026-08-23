impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();

        for x in nums {
            if !seen.insert(x) {
                return true;
            }
        }
        return false;
    }
}

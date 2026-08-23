impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counts = HashMap::new();

        for n in nums {
            *counts.entry(n).or_insert(0) += 1;
        }

        let mut freq_vec: Vec<(i32, i32)> = counts.into_iter().collect();
        freq_vec.sort_unstable_by(|a, b| b.1.cmp(&a.1));

        freq_vec.into_iter().take(k as usize).map(|pair| pair.0).collect()

    }
}

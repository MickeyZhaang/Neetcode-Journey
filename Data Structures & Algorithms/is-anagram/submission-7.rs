impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }

        let mut counts = HashMap::new();

        for c in s.chars() {
            if counts.contains_key(&c) {
                let cur_val = counts.get_mut(&c).unwrap();
                *cur_val += 1;
            } else {
                counts.insert(c, 1);
            }
        }

        for c in t.chars() {
            if counts.contains_key(&c) {
                let cur_val = counts.get_mut(&c).unwrap();
                *cur_val -= 1;
            } else {
                return false;
            }
        }

        for val in counts.values() {
            if *val != 0 {
                return false;
            }
        }
        return true;

    }
}

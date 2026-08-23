impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();

        for s in strs {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort_unstable();
            let key: String = chars.into_iter().collect();

            if groups.contains_key(&key) {
                let group = groups.get_mut(&key).unwrap();
                group.push(s);
            } else {
                groups.insert(key, vec![s]);
            }
        }
        groups.into_values().collect()

    }
}

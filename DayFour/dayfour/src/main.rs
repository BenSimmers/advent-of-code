use std::fs;

fn part1(){
    let answer  = fs::read_to_string("src/input.txt").unwrap().lines()
        .map(|line| {
            return line
                .replace(",", " ")
                .replace("-", " ")
                .split(" ")
                .map(|v| v.parse::<i32>().unwrap_or_default())
                .collect::<Vec<i32>>()
                .chunks_exact(4)
                .map(|chunk| {
                    let mut i = chunk[0]..=chunk[1];
                    let j = chunk[2]..=chunk[3];

                    //part 1
                    if (i.contains(&chunk[2]) && i.contains(&chunk[3])) || (j.contains(&chunk[0]) && j.contains(&chunk[1]))
                    {
                        1
                    } else {
                        0
                    }
                })
                .next()
                .unwrap();
        })
        .fold(0, |acc, v| acc + v);

    println!("{answer }");
}

fn part2() {
    let answer  = fs::read_to_string("src/input.txt").unwrap().lines()
        .map(|line| {
            return line
                .replace(",", " ")
                .replace("-", " ")
                .split(" ")
                .map(|v| v.parse::<i32>().unwrap_or_default())
                .collect::<Vec<i32>>()
                .chunks_exact(4)
                .map(|chunk| {
                    let mut i = chunk[0]..=chunk[1];
                    let j = chunk[2]..=chunk[3];

                    //part 2
                    if i.any(|v| j.contains(&v)) {
                        1
                    } else {
                        0
                    }
                })
                .next()
                .unwrap();
        })
        .fold(0, |acc, v| acc + v);

    println!("{answer }");
}


fn main() {
    part1();
    part2();
}
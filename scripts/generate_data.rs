use std::fs::File;
use std::io::Write;
use rand::Rng;

fn main() {
    let mut file = File::create("float_data3.csv").expect("Erreur création fichier");
    writeln!(file, "a,b").unwrap(); // entête CSV

    let mut rng = rand::rng();
    for _ in 0..10 {
        let a: f64 = rng.random_range(-3.0..3.0);
        let b: f64 = rng.random_range(-3.0..3.0);
        writeln!(file, "{},{}", a, b).unwrap();
    }
}

use std::fs::File;
use std::io::{BufRead, BufReader};
use tfhe::prelude::*;
use tfhe::{generate_keys, set_server_key, ConfigBuilder, FheInt64};

//const N: usize = 100;
const SCALE: f64 = 1e3; // Peut essayer aussi 1e6 

fn main() {
    let file = File::open("./données/float_data.csv").expect("Erreur ouverture fichier");
    let reader = BufReader::new(file);

    let config = ConfigBuilder::default().build();
    let (client_key, server_keys) = generate_keys(config);
    set_server_key(server_keys);

    let mut abs_errors1 = Vec::new();
    let mut rel_errors1 = Vec::new();
    let mut abs_errors2 = Vec::new();
    let mut rel_errors2 = Vec::new();
    let mut abs_errors3 = Vec::new();
    let mut rel_errors3 = Vec::new();
    let mut abs_errors4 = Vec::new();
    let mut rel_errors4 = Vec::new();

    for (i, line) in reader.lines().enumerate() {
        if i == 0 { continue; } // skip header
        let line = line.unwrap();
        let parts: Vec<f64> = line.split(',').map(|s| s.parse().unwrap()).collect();
        let (a, b) = (parts[0], parts[1]);

        let enc_a = (a * SCALE).round() as i64;
        let enc_b = (b * SCALE).round() as i64;

        let fhe_a = FheInt64::encrypt(enc_a, &client_key);
        let fhe_b = FheInt64::encrypt(enc_b, &client_key);
        
        let fhe_result1 = &fhe_a + &fhe_b;
        let fhe_result2 = &fhe_a - &fhe_b;
        let fhe_result3 = &fhe_a * &fhe_b;
        let fhe_result4 = &fhe_a / &fhe_b;



        let decrypted1: i64 = fhe_result1.decrypt(&client_key);
        let decrypted2: i64 = fhe_result2.decrypt(&client_key);
        let decrypted3: i64 = fhe_result3.decrypt(&client_key);
        let decrypted4: i64 = fhe_result4.decrypt(&client_key);
        
        let decoded1 = decrypted1 as f64 / SCALE;
        let decoded2 = decrypted2 as f64 / SCALE;
        let decoded3 = decrypted3 as f64 / SCALE;
        let decoded4 = decrypted4 as f64 / SCALE;

        let expected1 = a + b;
        let expected2 = a - b;
        let expected3 = a * b;
        let expected4 = a / b;

        let abs_error1 = (decoded1 - expected1).abs();
        let rel_error1 = abs_error1 / expected1.abs().max(1e-8);
        let abs_error2 = (decoded2 - expected2).abs();
        let rel_error2 = abs_error2 / expected2.abs().max(1e-8);
        let abs_error3 = (decoded3 - expected3).abs();
        let rel_error3 = abs_error3 / expected3.abs().max(1e-8);
        let abs_error4 = (decoded4 - expected4).abs();
        let rel_error4 = abs_error4 / expected4.abs().max(1e-8);

        abs_errors1.push(abs_error1);
        rel_errors1.push(rel_error1);
        abs_errors2.push(abs_error2);
        rel_errors2.push(rel_error2);
        abs_errors3.push(abs_error3);
        rel_errors3.push(rel_error3);
        abs_errors4.push(abs_error4);
        rel_errors4.push(rel_error4);
    }

    let mean_abs1: f64 = abs_errors1.iter().sum::<f64>() / abs_errors1.len() as f64;
    let mean_rel1: f64 = rel_errors1.iter().sum::<f64>() / rel_errors1.len() as f64;
    let mean_abs2: f64 = abs_errors2.iter().sum::<f64>() / abs_errors2.len() as f64;
    let mean_rel2: f64 = rel_errors2.iter().sum::<f64>() / rel_errors2.len() as f64;
    let mean_abs3: f64 = abs_errors3.iter().sum::<f64>() / abs_errors3.len() as f64;
    let mean_rel3: f64 = rel_errors3.iter().sum::<f64>() / rel_errors3.len() as f64;
    let mean_abs4: f64 = abs_errors4.iter().sum::<f64>() / abs_errors4.len() as f64;
    let mean_rel4: f64 = rel_errors4.iter().sum::<f64>() / rel_errors4.len() as f64;

    println!("---- Addition ----------");
    println!("Erreur absolue moyenne: {}", mean_abs1);
    println!("Erreur relative moyenne: {}", mean_rel1);
    println!("---- Soustraction ------");
    println!("Erreur absolue moyenne: {}", mean_abs2);
    println!("Erreur relative moyenne: {}", mean_rel2);
    println!("---- Multiplication ----");
    println!("Erreur absolue moyenne: {}", mean_abs3);
    println!("Erreur relative moyenne: {}", mean_rel3);
    println!("---- Division ----------");
    println!("Erreur absolue moyenne: {}", mean_abs4);
    println!("Erreur relative moyenne: {}", mean_rel4);
}

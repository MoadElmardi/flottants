//use num_bigint::BigUint;
//use tfhe::integer::bigint::StaticUnsignedBigInt;
use tfhe::prelude::*;
use tfhe::{generate_keys, set_server_key, ConfigBuilder, FheInt64};
use std::time::{Duration, Instant};

const N: usize = 100;
const SCALE: f64 = 1e3; 

fn mean(durations: &[Duration]) -> Duration {
    durations.iter().sum::<Duration>() / (durations.len() as u32)
}

fn std_dev(durations: &[Duration], mean: Duration) -> Duration {
    let var = durations
        .iter()
        .map(|d| {
            let diff = (*d).as_secs_f64() - mean.as_secs_f64();
            diff * diff
        })
        .sum::<f64>()
        / durations.len() as f64;
    Duration::from_secs_f64(var.sqrt())
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = ConfigBuilder::default().build();
    // Génération des clés
    let (client_key, server_keys) = generate_keys(config);
    set_server_key(server_keys);

    // Chiffrement des entiers
    let a = 1545.4568f64;
    let a_encode = (a * echelle) as u64;
    //let a = BigUint::from(150u128);

    let mut encrypt_times = Vec::with_capacity(N);
    let mut op_times = Vec::with_capacity(N);
    let mut op2_times = Vec::with_capacity(N);
    let mut op3_times = Vec::with_capacity(N);
    let mut op4_times = Vec::with_capacity(N);
    let mut op5_times = Vec::with_capacity(N);
    let mut op6_times = Vec::with_capacity(N);
    let mut op7_times = Vec::with_capacity(N);
    let mut decrypt_times = Vec::with_capacity(N);

    for _ in 0..N {
        let start_encrypt = Instant::now();
        let ctxt_a = FheUint64::try_encrypt(a_encode, &client_key)?;
        let encrypt_duration = start_encrypt.elapsed();

        // Opération homomorphe (shift)
        let start_op = Instant::now();
        let ctxt_result: FheUint64 = &ctxt_a >> 2_u64;
        let op_duration = start_op.elapsed();

        // Opération homomorphe (addition d'une constante)
        let start_op = Instant::now();
        let ctxt_result2 = &ctxt_a + 25u64;
        let op_duration2 = start_op.elapsed();

        // Opération homomorphe (multiplication par une constante)
        let start_op = Instant::now();
        let ctxt_result3 = &ctxt_a * 2u64;
        let op_duration3 = start_op.elapsed();

        let ctxt_a6 = ctxt_a.clone();
        let ctxt_a7 = ctxt_a.clone();

        // Opération homomorphe (ET binaire)
        let start_op = Instant::now();
        let ctxt_result5 = ctxt_a & 0u64;
        let op_duration5 = start_op.elapsed();

        // Opération homomorphe (NOT)
        let start_op = Instant::now();
        let ctxt_result6 = !ctxt_a6;
        let op_duration6 = start_op.elapsed(); 

        // Opération homomorphe (casting)

        let start_op = Instant::now();
        let ctxt_result4: FheUint16 = ctxt_a7.cast_into();
        let op_duration4 = start_op.elapsed();  

        // Opération homomorphe (OU binaire)
        let start_op = Instant::now();
        let ctxt_result7 = ctxt_a | 0_u64 ;
        let op_duration7 = start_op.elapsed();      

        // Déchiffrement
        let start_decrypt = Instant::now();
        let result: u64 = ctxt_result.decrypt(&client_key);
        let decrypt_duration = start_decrypt.elapsed();
        let result2: u64 = ctxt_result2.decrypt(&client_key);
        let result3: u64 = ctxt_result3.decrypt(&client_key);
        let result4: u16 = ctxt_result3.decrypt(&client_key);
        let result5: u64 = ctxt_result5.decrypt(&client_key);
        let result6: u64 = ctxt_result6.decrypt(&client_key);
        let result7: u64 = ctxt_result7.decrypt(&client_key);

        // Déencodage
        let result_flottant = result as f64 / echelle;
        let result_flottant2 = result2 as f64 / echelle;
        let result_flottant3 = result3 as f64 / echelle;
        let result_flottant4 = result4 as f64 / echelle;
        let result_flottant5 = result5 as f64 / echelle;
        let result_flottant6 = result6 as f64 / echelle;
        let result_flottant6 = result7 as f64 / echelle;


        // pour vérifier la validité
        result_prevu = a >> 2;
        let err_abs = (result_flottant - result_prevu).abs();
        let err_reel = err_abs / result_prevu.abs().max(1e-8);
        result_prevu2 = a + 25;
        let err_abs2 = (result_flottant2 - result_prevu2).abs();
        let err_reel2 = err_abs2 / result_prevu2.abs().max(1e-8);
        result_prevu3 = a * 2;
        let err_abs3 = (result_flottant3 - result_prevu3).abs();
        let err_reel3 = err_abs3 / result_prevu3.abs().max(1e-8);
        
        result_prevu5 = a & 0;
        let err_abs5 = (result_flottant5 - result_prevu5).abs();
        let err_reel5 = err_abs5 / result_prevu5.abs().max(1e-8);

        assert_eq!(result6, !a);
        assert_eq!(result7, a | 0);


        encrypt_times.push(encrypt_duration);
        op_times.push(op_duration);
        op2_times.push(op_duration2);
        op3_times.push(op_duration3);
        op4_times.push(op_duration4);
        op5_times.push(op_duration5);
        op6_times.push(op_duration6);
        op7_times.push(op_duration7);
        decrypt_times.push(decrypt_duration);
    }

    // Moyenne et écart-type
    let encrypt_mean = mean(&encrypt_times);
    let op_mean = mean(&op_times);
    let op2_mean = mean(&op2_times);
    let op3_mean = mean(&op3_times);
    let op4_mean = mean(&op4_times);
    let op5_mean = mean(&op5_times);
    let op6_mean = mean(&op6_times);
    let op7_mean = mean(&op7_times);
    let decrypt_mean = mean(&decrypt_times);

    let encrypt_std = std_dev(&encrypt_times, encrypt_mean);
    let op_std = std_dev(&op_times, op_mean);
    let op2_std = std_dev(&op2_times, op2_mean);
    let op3_std = std_dev(&op3_times, op3_mean);
    let op4_std = std_dev(&op4_times, op4_mean);
    let op5_std = std_dev(&op5_times, op5_mean);
    let op6_std = std_dev(&op6_times, op6_mean);
    let op7_std = std_dev(&op7_times, op7_mean);
    let decrypt_std = std_dev(&decrypt_times, decrypt_mean);

    println!("--- Résultats sur {N} répétitions ---");
    println!(
        "Chiffrement: moyenne = {:?}, écart-type = {:?}",
        encrypt_mean, encrypt_std
    );
    println!(
        "Shift  : moyenne = {:?}, écart-type = {:?}",
        op_mean, op_std
    );
    println!(
        "Addition d'une constante  : moyenne = {:?}, écart-type = {:?}",
        op2_mean, op2_std
    );
    println!(
        "Multiplication par une constante  : moyenne = {:?}, écart-type = {:?}",
        op3_mean, op3_std
    );
    println!(
        "Casting  : moyenne = {:?}, écart-type = {:?}",
        op4_mean, op4_std
    );
    println!(
        "ET binaire : moyenne = {:?}, écart-type = {:?}",
        op5_mean, op5_std
    );
    println!(
        "OU binaire  : moyenne = {:?}, écart-type = {:?}",
        op7_mean, op7_std
    );
    println!(
        "NOT  : moyenne = {:?}, écart-type = {:?}",
        op6_mean, op6_std
    );
    println!(
        "Déchiffrement: moyenne = {:?}, écart-type = {:?}",
        decrypt_mean, decrypt_std
    );

    Ok(())
}

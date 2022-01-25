#!/usr/bin/python3

import click
import vzz_conversion as vzzc


@click.command()
@click.option("--vzz", type=float,
              required=False, help="EFG value [V/m^2]")
@click.option("--w0", type=float,
              required=False, help="w0 value [Mrads/s]")
@click.option("--eta", type=float,
              required=True, help="Asymmetry parameter")
@click.option("--q", type=float,
              required=True, help="Nuclear quadrupole moment [bn]")
def cli(eta, q, vzz=0.0, w0=0.0):
    """cli tool for recalculation of EFG and w0 (omega_0)."""
    if vzz:
        w_0 = vzzc.vzz_to_w0(vzz, eta, q)
        print("w_0 = {:.4e} Mrad/s".format(w_0 * 1e-6))
    elif w0:
        V_zz = vzzc.w0_to_vzz(w0 * 1.0e6, eta, q * 1.0e-24)
        print("V_zz = {:.2e} V/cm^2".format(V_zz))

        
if __name__ == "__main__":
    cli()

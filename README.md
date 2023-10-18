# NetworkManager OpenConnect SSO Integration

This project, `networkmanager-openconnect-sso`, enhances NetworkManager with the capability of handling Azure AD (SAMLv2) authentication for Cisco SSL-VPNs by integrating `openconnect-sso`.

## Installation

To get started with `networkmanager-openconnect-sso`, clone the repository to your local machine:

```shell
git clone https://github.com/mschabhuettl/networkmanager-openconnect-sso.git
cd networkmanager-openconnect-sso
```

Follow the standard procedure for building and installing a NetworkManager extension on your system. Ensure you have the necessary dependencies like NetworkManager, OpenConnect, and the appropriate development libraries.

## Usage

After successful installation, `networkmanager-openconnect-sso` will be available as an extension within NetworkManager. You can establish VPN connections requiring Azure AD authentication through the standard NetworkManager interface.

Configure your VPN settings as you would with any standard connection, selecting the OpenConnect protocol with SSO authentication where required.

## Contributing

We encourage community participation in the development of `networkmanager-openconnect-sso`. If you wish to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

Please adhere to the highest standards for coding and documentation while contributing.

## Acknowledgments

- This project is built on the foundational work of `vlaci`, the creator of the original `openconnect-sso` script. Their efforts made this integration possible.

## License

`networkmanager-openconnect-sso` is licensed under the GPL-3.0 License, the same as the original `openconnect-sso` project. Refer to the [LICENSE](LICENSE) file for more details.

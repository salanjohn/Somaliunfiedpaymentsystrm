"""UnifiedPay Somalia - runnable demo CLI.

This simple script demonstrates how an interoperability layer can route
payments between providers and banks.
"""

from dataclasses import dataclass


@dataclass
class Payment:
    sender: str
    receiver: str
    amount_usd: float
    source_provider: str
    destination_provider: str


SUPPORTED_PROVIDERS = {
    "ZAAD",
    "EVC Plus",
    "Sahal",
    "Premier Bank",
    "Salaam Bank",
}


def validate_payment(payment: Payment) -> None:
    if payment.amount_usd <= 0:
        raise ValueError("Amount must be greater than 0.")
    if payment.source_provider not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported source provider: {payment.source_provider}")
    if payment.destination_provider not in SUPPORTED_PROVIDERS:
        raise ValueError(
            f"Unsupported destination provider: {payment.destination_provider}"
        )


def route_payment(payment: Payment) -> str:
    validate_payment(payment)

    if payment.source_provider == payment.destination_provider:
        route = f"direct ledger transfer in {payment.source_provider}"
    else:
        route = (
            "interoperability switch "
            f"({payment.source_provider} -> UnifiedPay -> {payment.destination_provider})"
        )

    return (
        f"SUCCESS: Sent ${payment.amount_usd:.2f} from {payment.sender} to "
        f"{payment.receiver} via {route}."
    )


def main() -> None:
    sample = Payment(
        sender="Asha",
        receiver="Hassan",
        amount_usd=25.0,
        source_provider="ZAAD",
        destination_provider="Premier Bank",
    )
    print(route_payment(sample))


if __name__ == "__main__":
    main()

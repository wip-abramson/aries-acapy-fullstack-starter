aca-py start \
    -it http '0.0.0.0' "$PORT" \
    -e "$AGENT_ENDPOINT" "${AGENT_ENDPOINT/http/ws}" \
    --auto-accept-requests  \
    --auto-respond-credential-proposal --auto-respond-credential-offer --auto-respond-credential-request --auto-store-credential \
    --auto-respond-presentation-proposal --auto-respond-presentation-request \
    --preserve-exchange-records \
    "$@"
# --------------------------------------------
# Stage 1: Builder stage (install dependencies)
# --------------------------------------------
    FROM ubuntu:22.04 AS builder

    # Install Python and set up the log directory
    RUN apt-get update && \
        apt-get install -y --no-install-recommends python3 libexpat1 && \
        mkdir -p /var/log && \
        rm -rf /var/lib/apt/lists/*
    
    # --------------------------------------------
    # Stage 2: Runtime stage (optimized)
    # --------------------------------------------
    FROM ubuntu:22.04
    
    # Copy necessary libraries from the builder stage
    COPY --from=builder /usr/bin/python3 /usr/bin/python3
    COPY --from=builder /usr/lib/python3.10 /usr/lib/python3.10
    COPY --from=builder /usr/lib/x86_64-linux-gnu/libexpat.so.1 /usr/lib/x86_64-linux-gnu/libexpat.so.1
    COPY --from=builder /var/log /var/log
    
    # Create a non-root user and set permissions
    RUN useradd -m calculator-user && \
        chown -R calculator-user:calculator-user /var/log
    
    WORKDIR /app
    
    # Copy application scripts and Python file
    COPY app/calculator.py .
    COPY app/entrypoint.sh .
    COPY scripts/healthcheck.sh .
    
    # Make scripts executable
    RUN chmod +x entrypoint.sh healthcheck.sh
    
    # Switch to non-root user
    USER calculator-user
    
    # Healthcheck using the custom script
    HEALTHCHECK --interval=30s --timeout=5s \
      CMD ./healthcheck.sh
    
    # Use the custom entrypoint script
    ENTRYPOINT ["./entrypoint.sh"]
    
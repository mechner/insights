

* We have a broad architectural strategy to steadily replace any systems' "raw" dependencies
  on bl (via direct database access, JMS, and nested maps) with an indirect dependency via
  a well-managed API - either to bl itself or to common upstream systems or services.

# Definitions

* System: a set of applications with a unified build & release cycle.
  Some systems are contained in a single repo and a release version tags a build, and some
  span multiple repos; in this case the release version is an alias that defines a set of versioned
  artifacts that are deployed together. (should they be packaged into a uber jar? do we care?)
* API or Protocol: A collection of related schemas and topics (for kafka) or endpoints
  (for REST) that govern the interaction between two or more systems. An API is implemented by a system.
* Commit: Code is merged.
* Build: Code is compiled into an Artifact.
* Version: The commit and artifact are tagged (e.g. sys-1.2.3).
* Publish: The artifact is stored in Artifactory.
* Release Package (N.): a set of artifacts that may be deployed an environment. Examples include
  (BondLink 26.1.1.0, PreTrade 12.0.1.)
* Deploy: Move release package(s) into an Environment.
* Release (V.): The functionality is toggled "ON" for Users (seems to be standard termonology but maybe confusing for us?)

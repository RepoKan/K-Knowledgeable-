# Compose Multiplatform Toolchain Reviews — 1–14 September 2026

Status: Confirmed external-toolchain research  
Authority: A6 — official external release notes and compatibility documentation  
Production effect: None. This report does not authorize a Production toolchain upgrade.

## Review: 1–7 September 2026

Overall: no new stable release required an immediate production upgrade. The important development was an AGP 10 migration warning affecting the existing Compose Multiplatform module structure.

| Component | Change | CMP impact | Action |
|---|---|---|---|
| AGP | The AGP 9.4 preview notes documented Gradle 9.6, API 37 support, and that the new Variant API becomes mandatory in AGP 10. A temporary per-module **android.newDsl.optOut** remains available before AGP 10. [AGP 9.4 notes](https://developer.android.com/build/releases/agp-9-4-0-release-notes) | High migration relevance, but preview-only. The opt-out is temporary and does not solve the CMP architecture issue. | Do not upgrade production to AGP 9.4. Prepare the module split required before AGP 10. |
| Kotlin | Kotlin 2.4.20-RC3 was published September 2 with a compiler fix for a suspend-conversion ClassCastException. It remained a prerelease at the time of this review. [Kotlin releases](https://github.com/JetBrains/kotlin/releases) | Low unless the project reproduces that compiler crash. | Wait for Kotlin 2.4.20 stable. |
| KSP | No new release. Latest remained KSP 2.3.11 from August 3, including isolated-project support, Android-test task fixes, cache fixes, and improved KSP2 deprecation messaging. [KSP releases](https://github.com/google/ksp/releases) | No new compatibility change. | Do not change KSP independently; validate it with Kotlin, Room, and AGP. |
| Gradle | No new release; Gradle 9.7.1 from August 19 remained current. [Gradle releases](https://gradle.org/releases/) | Potential version gap: Kotlin 2.4.10 was fully supported only through Gradle 9.5 and AGP 9.1. | Avoid AGP 9.4 plus Kotlin 2.4.10 in production. |
| JDK | JDK 27 remained a release candidate, with GA planned for September 15. Gradle 9.7.1 could not run on JVM 27. | Low immediate impact. | Keep Gradle running on JDK 21. |

### Compatibility finding

Kotlin 2.2.20 supported AGP only through 8.11.1, making Kotlin 2.2.20 plus AGP 9.1 outside Kotlin's fully supported range.

Legacy KMP use of **com.android.library** relies on deprecated AGP APIs expected to disappear in AGP 10. A KMP module using **com.android.application** has no direct replacement and must be split into a separate Android application module and shared KMP library. [Android-KMP migration guidance](https://developer.android.com/kotlin/multiplatform/plugin)

### Recommended action

- Keep the production toolchain unchanged.
- Prioritize the **androidApp + shared KMP library** separation.
- Treat **android.newDsl.optOut** only as a temporary escape hatch.
- Test AGP, Gradle, Kotlin, KSP, Compose Multiplatform, Room, and JDK as one compatibility matrix.

### Review questions

1. Does **composeApp** still apply both Kotlin Multiplatform and **com.android.application**?
2. Which Android-only features—product flavors, build types, BuildConfig, AIDL, or native builds—must remain outside the new single-variant KMP library?
3. Should the next controlled baseline use Kotlin 2.4.x, AGP no higher than Kotlin's documented limit, and JDK 21?
4. Do all KSP processors pass Android, iOS, clean-build, and incremental-build tests?

---

## Review: 8–14 September 2026

Three stable releases are relevant: Kotlin 2.4.20, KSP 2.3.12, and Room 2.8.5. No emergency upgrade is required, but KSP 2.3.12 cannot be adopted on an AGP 8.11-or-earlier baseline.

### What changed

| Component | Release and change | Impact | Action |
|---|---|---|---|
| Kotlin/KGP | **2.4.20 stable — September 7.** Includes Compose compiler fixes for cross-module getter/setter miscompilation, generic composable singletons, and cross-module composable overrides. Kotlin/Native adds improved incremental compilation, Swift export improvements, and generated Package.swift output for XCFrameworks with SwiftPM dependencies. [Release notes](https://kotlinlang.org/docs/whatsnew2420.html) · [Full changelog](https://github.com/JetBrains/kotlin/releases) | Medium for Android, iOS, shared UI, and CI. Native incremental compilation remains beta and opt-in. SwiftPM packaging changes matter when distributing XCFrameworks through SwiftPM. | Suitable for a controlled migration branch. Align Compose and serialization compiler plugins with Kotlin 2.4.20. |
| KSP | **2.3.12 stable — September 9.** Fixes incomplete declarations returned from KMP KLibs, Android-KMP lint task dependencies, and CLI hangs after processor failure. It adds opt-in processor support for explicit backing fields and raises the minimum supported AGP to 8.12.0. [KSP releases](https://github.com/google/ksp/releases) | High build-compatibility impact. KSP 2.3.12 has no supported overlap with Kotlin 2.2.20/2.2.21's AGP maximum of 8.11.1. | Do not upgrade KSP independently. Adopt it only with Kotlin 2.4.20 and AGP 8.12 or newer. |
| Room KMP | **2.8.5 stable — September 9.** Suspending queries and invalidation-tracker operations now throw IllegalStateException when called after RoomDatabase.close(). No schema format, migration API, driver, or code-generation change was listed. [Room release notes](https://developer.android.com/jetpack/androidx/releases/room#2.8.5) | Medium shared-data lifecycle impact. Late DAO calls or surviving Flow collectors may now fail explicitly on Android and iOS. | Upgrade after KSP/toolchain alignment. Cancel database-owning work and collectors before close. |
| Compose Multiplatform | **1.13.0-alpha01 — September 10, preview.** Raises Android minSdk to 24; removes ComposeUiFlags.useLegacyRenderNodeLayers; stops bundling Skottie in Skiko core; deletes deprecated compose.web.targets(...). iOS gains Dynamic Type scaling, preferred-size reporting for UIKit/SwiftUI embedding, and text-input, accessibility, and navigation fixes. [Compose releases](https://github.com/JetBrains/compose-multiplatform/releases) | Medium future impact but low immediate impact. The minSdk and removed APIs are migration gates. | Keep production on Compose 1.12.0. Test 1.13 separately only for a directly relevant issue. |
| Kotlin serialization | No stable release this week. Stable remained 1.11.0; 1.12.0-RC remained prerelease. [Serialization releases](https://github.com/Kotlin/kotlinx.serialization/releases) | None immediately. The compiler plugin follows Kotlin; the runtime has an independent version lifecycle. | Keep the stable runtime. |
| Coroutines | No new release; 1.11.0 remained current. Kotlin 2.4.20 adds experimental JVM exception stack-trace recovery integration without requiring a coroutines migration. [Coroutines releases](https://github.com/Kotlin/kotlinx.coroutines/releases) | Low. | No action. |
| moko-permissions | No new release. Latest remained 0.20.1 from August 28, containing the Android activity leak fix. [moko-permissions releases](https://github.com/icerockdev/moko-permissions/releases) | No new compatibility signal. | If below 0.20.1, include the upgrade in normal permission lifecycle testing. |

### Compatibility constraints and carry-over items

- Kotlin 2.4.20 officially supports Gradle 7.6.3–9.7.0 and AGP 8.5.2–9.3.1.
- Kotlin 2.2.20–2.2.21 supports Gradle 7.6.3–8.14 and AGP 7.3.1–8.11.1.
- KSP 2.3.12 therefore requires leaving the Kotlin 2.2.x/AGP 8.11 baseline.
- The smallest coordinated step is Kotlin 2.4.20 plus AGP 8.12 or newer, using the selected AGP's required Gradle version and keeping Gradle at or below 9.7.0. [Kotlin compatibility matrix](https://kotlinlang.org/docs/gradle-configure-project.html)
- Carry-over, high severity: split any KMP module using **com.android.application** into an Android app and shared KMP library before AGP 10.
- For the Android-KMP plugin, use **android {}** from AGP 8.12. **androidLibrary {}** is deprecated.
- AGP 9.4 remains preview-only and is outside Kotlin 2.4.20's fully supported AGP range.
- Gradle 9.7.1 remains just beyond Kotlin's documented maximum of 9.7.0.
- Keep JDK 21 as the CI and Android Studio Gradle JVM.
- No meaningful new stable Xcode, CocoaPods, JDK, Compose resource, Lifecycle, Navigation, serialization, coroutines, or moko-permissions migration was published in this review period.

### Dependency-ordered upgrade sequence

#### Mandatory gating work

1. Keep CI and Android Studio's Gradle JVM pinned to JDK 21.
2. Complete the Android application/shared-KMP module separation before AGP 10.
3. Do not combine KSP 2.3.12 with AGP below 8.12.

#### Recommended validation upgrade

1. In one migration branch, move atomically to Kotlin/KGP 2.4.20 plus AGP 8.12–9.3.1 and the selected AGP's required Gradle version, capped at Gradle 9.7.0.
2. Change Android-KMP **androidLibrary {}** to **android {}** where applicable.
3. Explicitly re-enable Android resources, Java compilation, host tests, and device tests where required by the new Android-KMP plugin.
4. Align Kotlin serialization and Compose compiler plugin versions with Kotlin 2.4.20.
5. Upgrade KSP to 2.3.12, then Room to 2.8.5; regenerate and diff exported Room schemas.
6. Keep Compose Multiplatform 1.12.0 and moko-permissions 0.20.1 fixed while validating the toolchain.

#### Optional

- Evaluate Compose 1.13 alpha separately.
- Enable Kotlin/Native incremental compilation only in an experimental CI lane first.

### Focused regression matrix

| Area | Required checks |
|---|---|
| Clean and incremental build | Clean Android assemble, iOS simulator link, iosArm64 release link, warm rebuild, configuration/build cache, and KSP regeneration after entity or DAO changes |
| Android device | Install and upgrade on the supported minimum API and Sunmi P3; Room queries and transactions; permission grant, deny, permanent denial, settings return; process death and recreation |
| iOS simulator | Fresh DB creation, migration, DAO Flow updates, navigation and back gestures, text input, resource loading, background and foreground |
| iOS physical device | Location, Bluetooth, camera, and notification permission flows; settings return; denied and restricted states; database persistence and lifecycle transitions |
| Compose UI | Cross-module composables, default parameters, state restoration, text-field focus, accessibility scaling and VoiceOver, dialogs, popups, and navigation transitions |
| Room lifecycle | Migration schema verification, concurrent reads and writes, collector cancellation before close, deliberate late query after close, and database reopen |
| Release builds | R8/minified Android build, signed APK/AAB smoke test, release XCFramework, CocoaPods or SwiftPM integration, and generated Package.swift when applicable |

### Developer-review questions

1. Are we ready to replace the Kotlin 2.2.x/AGP 8.11 ceiling with one coordinated Kotlin 2.4.20 plus AGP 8.12-or-newer migration?
2. Can any ViewModel, repository scope, or long-lived Room Flow outlive RoomDatabase.close()?
3. Does any Android target still require API 23 or lower, blocking a future Compose 1.13 adoption?
4. Does iOS consume the shared framework through CocoaPods or distribute an XCFramework through SwiftPM?

## Source classification

This is sanitized engineering research based on official public documentation. It is not an approved host specification, Production source, runtime evidence, or authorization to modify Production behavior.

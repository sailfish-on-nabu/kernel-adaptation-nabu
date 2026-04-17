# Device details
%define device nabu

# Kernel target architecture
%define kernel_arch arm64

%define makeopts LLVM=1 LLVM_IAS=1
%define hostldflags ""

# Crossbuild toolchain to use
%define crossbuild aarch64
%define clangtriple aarch64-suse-linux-
%define crosscompile aarch64-suse-linux-
%define crosscompile32 arm-linux-androideabi-

%define kcflags "KCFLAGS=-Wno-error=implicit-function-declaration -Wno-error=missing-prototypes"

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu aarch64

# Defconfig to pick-up
%define defconfig defconfig_nabu

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# Apply Patches
%define apply_patches 1

# Build uImage
##define build_uImage 1

# Build zImage
##define build_zImage 1

# Build and pick-up the following devicetrees
%define devicetrees qcom/sm8150-xiaomi-nabu.dtb

Version:        6.14.11
Release:        1

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc

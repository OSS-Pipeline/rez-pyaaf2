CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# pyaaf2
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    PYAAF_URL pyaaf2/pyaaf2-${REZ_BUILD_PROJECT_VERSION}.tar.gz
    https://files.pythonhosted.org/packages/fb/c1/67ceeba190efa1e6281b214c7d827cd05e7c8b82ba456a043f0ba5cc3eb4/pyaaf2-${REZ_BUILD_PROJECT_VERSION}.tar.gz
)

# In the case of a Python pip wheel file, we do not have any archive to extract, so we can just execute our Bash
# script(s) inside an "execute_process" macro.
execute_process(
    COMMAND
    bash ${CMAKE_SOURCE_DIR}/install.sh ${PYAAF_URL}
    RESULT_VARIABLE RETURN_CODE
)

# We check that the execute_process() macro terminated properly.
# If not, we abort the process.
if(RETURN_CODE EQUAL "1")
    message(FATAL_ERROR "[CMAKE] Install script returned an error code. Aborting...")
endif()

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] pyaaf2-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)

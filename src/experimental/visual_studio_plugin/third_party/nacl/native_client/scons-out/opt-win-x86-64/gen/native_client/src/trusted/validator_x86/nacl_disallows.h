/* \gen\native_client\src\trusted\validator_x86\nacl_disallows.h
 * THIS FILE IS AUTO_GENERATED DO NOT EDIT.
 *
 * This file was auto-generated by enum_gen.py
 * from file nacl_disallows.enum
 */

#ifndef _GEN_NATIVE_CLIENT_SRC_TRUSTED_VALIDATOR_X86_NACL_DISALLOWS_H__
#define _GEN_NATIVE_CLIENT_SRC_TRUSTED_VALIDATOR_X86_NACL_DISALLOWS_H__
typedef enum NaClDisallowsFlag {
  NaClTooManyPrefixBytes = 0,
  NaClMarkedIllegal = 1,
  NaClMarkedInvalid = 2,
  NaClMarkedSystem = 3,
  NaClHasBadSegmentPrefix = 4,
  NaClCantUsePrefix67 = 5,
  NaClMultipleRexPrefix = 6,
  NaClDisallowsFlagEnumSize = 7, /* special size marker */
} NaClDisallowsFlag;

/* Returns the name of an NaClDisallowsFlag constant. */
extern const char* NaClDisallowsFlagName(NaClDisallowsFlag name);

#endif /* _GEN_NATIVE_CLIENT_SRC_TRUSTED_VALIDATOR_X86_NACL_DISALLOWS_H__ */

# =====================================================================================================================
# WARNING: DO NOT EMPTY THIS SET!
# =====================================================================================================================
# This set, `exceptions_set`, must always contain at least one dummy entry. If this set is empty, the code will 
# throw an error when trying to add new entries using the `.add()` method. The `exceptions_set` is used to store 
# live updates from Times Now that should not be re-sent as WhatsApp messages. This prevents duplicate messages 
# from being sent each time the application runs.
#
# If you want to avoid sending messages for certain updates, include those updates here as strings.
# This ensures that those updates are skipped in future runs.
# =====================================================================================================================

exceptions_set = {
    "Jun 24, 2024 19:16 IST SBI Clerk Mains Result 2024 Expected DateSBI Clerk Mains 2024 exam was conducted between February 25 and March 2, 2024. SBI result was earlier expected to be announced in May but reports claim that it got deferred due to the Lok Sabha 2024 elections. With 20 days passed since election result, aspirants are waiting for results to be out.",
    "Jun 24, 2024 18:11 IST SBI Clerk Mains Result 2024: Expected SoonSBI Clerk Mains Result 2024 for thousands of aspirants will be released soon. Sources claim that the result will be released this week itself on sbi.co.in. Candidates are advised to keep an eye here for not missing updates related to the result release announcement.",
    
}
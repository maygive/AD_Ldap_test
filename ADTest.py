
import sys
import ldap
def authenticate(username, password):
    try:
#         WATER\DW_Report
# Dw@mWa2565
        # print(username)
        # user = "%s%s"%(username,"@fpo.go.th")
        # password = decode(password1).decode("utf-8")

        # connectLDAP = ldap.initialize("ldap://%s"%"203.154.71.182")
        # print(user)

        # connectLDAP = ldap.initialize("ldap://10.252.38.18")

        
##        connectLDAP = ldap.initialize("ldap://water.mwa:389")
        connectLDAP = ldap.initialize("ldap://ldap.forumsys.com:389")
        print("dddddffffffff")
##        print(connectLDAP)
##        print(password)

        connectLDAP.protocol_version = ldap.VERSION3
        connectLDAP.set_option(ldap.OPT_REFERRALS, 0)
        print("cfcfcf")

        connectLDAP.simple_bind_s("cn=read-only-admin,dc=example,dc=com", "password")

##        connectLDAP.simple_bind_s("DW_Report", "Dw@mWa2565")
        
        # connectLDAP.simple_bind_s(username, password)
        
        print("ddddd")


        # base_dn = 'ou=scientists,dc=example,dc=com'
        # retrieveAttributes = ["uniquemember","displayName"]
        # searchFilter = "(&(objectClass=*)(sAMAccountName=" + "einstein" + "))"
        # result = connectLDAP.search_s(base_dn, ldap.SCOPE_SUBTREE,searchFilter,retrieveAttributes,0)
        # print(result)


        # base_dn = 'dc=fpo,dc=go,dc=th'
        # retrieveAttributes = ["uniquemember","displayName"]
        # searchFilter = "(&(objectClass=*)(sAMAccountName=" + "admin@fpo.go.th" + "))"
        # result = connectLDAP.search_s(base_dn, ldap.SCOPE_SUBTREE,searchFilter,retrieveAttributes,0)

        # print("ddd")
        # print(result)
        # print("gggg")
        # print( connectLDAP.simple_bind_s(user, password))
    except ldap.CONNECT_ERROR:
        return("CONNECT_ERROR")
    except ldap.BUSY:
        return("BUSY")
    except ldap.TIMEOUT:
        return("TIMEOUT")
    except ldap.INVALID_CREDENTIALS:
        return("Invalid credentials")
    except ldap.SERVER_DOWN:
        return("Server down")
    except ldap.LDAPError as e:
        if type(e.message) == dict and e.message.has_key('desc'):
            return("Other LDAP error: " + e.message['desc'])
        else:
            return("Other LDAP error: " +e)
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        line_number = exception_traceback.tb_lineno
        print("Line number: ", line_number)
        print("Error: " + str(e))
        return ({"status": "Error: " + str(e),"Line number": line_number})
    finally:
        print("hiiii")
        connectLDAP.unbind_s()
    print("finish")
    return "Succesfully authenticated"


print(authenticate("ait_dev","dev_fpo@"))

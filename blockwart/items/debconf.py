from blockwart.items import Item, ItemStatus
from blockwart.utils import LOG
from blockwart.utils.text import bold
from blockwart.utils.text import mark_for_translation as _


def debconf_selection(node, pkg_name, key):
    result = node.run(
        "debconf-get-selections | grep -E \"^{}\s+{}\s+\" | awk '{}'".format(
            pkg_name,
            key,
            r"{ print $3,$4,$5,$6,$7,$8,$9,$10 }"
        ),
        may_fail=True,
    )
    if result.return_code != 0 or not result.stdout:
        return False
    else:
        return result.stdout


class DebConfSelection(Item):
    """
    Interface to debconf
    """
    BUNDLE_ATTRIBUTE_NAME = "debconf_selections"
    DEPENDS_STATIC = []
    # "pkg_apt:debconf-utils" 
    ITEM_ATTRIBUTES = {
        'pkg_name': None,
        'value': "",
    }
    ITEM_TYPE_NAME = "debconf_selection"
    PARALLEL_APPLY = False
    REQUIRED_ATTRIBUTES = ['pkg_name', 'value']

    def __repr__(self):
        return "<DebConfSelection pkg_name:{} key:{} value:{}>".format(
            self.attributes['pkg_name'],
            self.name,
            self.attributes['value'],
        )

    def ask(self, status):
        if not status.info['exists']:
            return _("'{}' not found in debconf-selections").format(self.name)

        return "{}: '{}' > '{}'\n".format(
            self.attributes['pkg_name'],
            status.info['value'],
            self.attributes['value'],
        )

    def fix(self, status):
        if not status.info['exists']:
            LOG.info(_("{}:{}: creating...").format(self.node.name, self.id))
        else:
            LOG.info(_("{}:{}: updating...").format(self.node.name, self.id))

        self.node.run("echo '{} {} {}' | debconf-set-selections".format(
            self.attributes['pkg_name'],
            self.name,  
            self.attributes['value'],
        ))
        
    def get_status(self):
        value = debconf_selection(self.node, self.attributes['pkg_name'], self.name)
        value_exists = (value)
        item_status = (value == self.attributes['value'])
        return ItemStatus(
            correct=item_status,
            info={
                'exists': value_exists,
                'value': value,
            },
        )